from flask import Flask, request, jsonify, send_file
import akshare as ak
import pandas as pd
from datetime import datetime, timedelta
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    code = request.json.get('code')
    if not code:
        return jsonify({'error': '请输入股票代码'})
    
    try:
        # 计算一年前的日期
        end_date = datetime.now().strftime('%Y%m%d')
        start_date = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')
        
        # 使用akshare获取K线数据
        stock_zh_a_hist_df = ak.stock_zh_a_hist(
            symbol=code,
            period="daily",
            start_date=start_date,
            end_date=end_date,
            adjust="qfq"
        )
        
        # 准备返回数据
        data = []
        for _, row in stock_zh_a_hist_df.iterrows():
            data.append({
                'date': row['日期'],
                'open': float(row['开盘']),
                'close': float(row['收盘']),
                'low': float(row['最低']),
                'high': float(row['最高']),
                'volume': float(row['成交量'])
            })
        
        return jsonify({'data': data, 'code': code})
    except Exception as e:
        return jsonify({'error': f'错误：{str(e)}'})

@app.route('/download_csv', methods=['POST'])
def download_csv():
    code = request.json.get('code')
    if not code:
        return jsonify({'error': '请输入股票代码'})
    
    try:
        # 计算一年前的日期
        end_date = datetime.now().strftime('%Y%m%d')
        start_date = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')
        
        # 使用akshare获取K线数据
        stock_zh_a_hist_df = ak.stock_zh_a_hist(
            symbol=code,
            period="daily",
            start_date=start_date,
            end_date=end_date,
            adjust="qfq"
        )
        
        # 创建CSV文件
        csv_buffer = io.BytesIO()
        # 先写入字符串，再编码为字节
        csv_content = stock_zh_a_hist_df.to_csv(index=False, encoding='utf-8-sig')
        csv_buffer.write(csv_content.encode('utf-8-sig'))
        csv_buffer.seek(0)
        
        # 发送文件
        return send_file(
            csv_buffer,
            as_attachment=True,
            download_name=f'{code}.csv',
            mimetype='text/csv'
        )
    except Exception as e:
        return jsonify({'error': f'错误：{str(e)}'})

if __name__ == '__main__':
    # 确保index.html存在
    if not os.path.exists('index.html'):
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write('''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A股股票K线分析</title>
    <!-- ECharts -->
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .input-section {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        input[type="text"] {
            width: 200px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-left: 10px;
        }
        button:hover {
            background-color: #45a049;
        }
        .chart-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            height: 500px;
        }
        .download-section {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }
        #download-btn {
            background-color: #2196F3;
        }
        #download-btn:hover {
            background-color: #0b7dda;
        }
        .error-message {
            color: red;
            margin-top: 10px;
        }
        .loading {
            margin-top: 10px;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>A股股票K线分析</h1>
    
    <div class="input-section">
        <label for="stock-code">股票代码：</label>
        <input type="text" id="stock-code" placeholder="例如：600000">
        <button id="query-btn">查询</button>
        <div id="loading" class="loading" style="display: none;">加载中...</div>
        <div id="error-message" class="error-message"></div>
    </div>
    
    <div class="chart-container">
        <div id="kline-chart" style="width: 100%; height: 100%;"></div>
    </div>
    
    <div class="download-section">
        <button id="download-btn">下载CSV数据</button>
    </div>
    
    <script>
        // 初始化ECharts实例
        var chart = echarts.init(document.getElementById('kline-chart'));
        var currentCode = '';
        
        // 查询股票数据
        document.getElementById('query-btn').addEventListener('click', async function() {
            var code = document.getElementById('stock-code').value.trim();
            var errorDiv = document.getElementById('error-message');
            var loadingDiv = document.getElementById('loading');
            
            if (!code) {
                errorDiv.innerText = "请输入股票代码";
                return;
            }
            
            // 清空错误信息
            errorDiv.innerText = "";
            loadingDiv.style.display = "block";
            
            try {
                // 发送请求获取数据
                var response = await fetch('/get_stock_data', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ code: code })
                });
                
                var result = await response.json();
                
                if (result.error) {
                    errorDiv.innerText = result.error;
                } else {
                    currentCode = result.code;
                    updateChart(result.data);
                }
            } catch (error) {
                errorDiv.innerText = "网络错误，请稍后重试";
            } finally {
                loadingDiv.style.display = "none";
            }
        });
        
        // 下载CSV数据
        document.getElementById('download-btn').addEventListener('click', async function() {
            if (!currentCode) {
                document.getElementById('error-message').innerText = "请先查询股票数据";
                return;
            }
            
            try {
                // 发送请求下载数据
                var response = await fetch('/download_csv', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ code: currentCode })
                });
                
                if (!response.ok) {
                    throw new Error('下载失败');
                }
                
                // 处理下载
                var blob = await response.blob();
                var url = URL.createObjectURL(blob);
                var a = document.createElement('a');
                a.href = url;
                a.download = currentCode + '.csv';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            } catch (error) {
                document.getElementById('error-message').innerText = "下载失败，请稍后重试";
            }
        });
        
        // 更新图表函数
        function updateChart(data) {
            var option = {
                title: {
                    text: '股票K线图',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'axis',
                    formatter: function(params) {
                        var item = params[0];
                        return item.name + '<br/>'
                            + '开盘: ' + item.value[1] + '<br/>'
                            + '收盘: ' + item.value[2] + '<br/>'
                            + '最低: ' + item.value[3] + '<br/>'
                            + '最高: ' + item.value[4] + '<br/>'
                            + '成交量: ' + item.value[5];
                    }
                },
                xAxis: {
                    type: 'category',
                    data: data.map(function(item) { return item.date; }),
                    boundaryGap: false
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    name: 'K线',
                    type: 'candlestick',
                    data: data.map(function(item) {
                        return [item.open, item.high, item.low, item.close];
                    }),
                    itemStyle: {
                        color: '#ef4136',
                        color0: '#4caf50',
                        borderColor: '#ef4136',
                        borderColor0: '#4caf50'
                    }
                }]
            };
            chart.setOption(option);
        }
        
        // 响应式调整
        window.addEventListener('resize', function() {
            chart.resize();
        });
    </script>
</body>
</html>
''')
    
    # 启动服务器
    app.run(debug=True, port=8000, host='localhost')
