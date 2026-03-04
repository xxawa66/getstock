import streamlit as st
import akshare as ak
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go

st.set_page_config(
    page_title="A股股票K线分析",
    page_icon="📈",
    layout="wide"
)

st.title("📈 A股股票K线分析")
st.markdown("---")

col1, col2 = st.columns([1, 4])

with col1:
    stock_code = st.text_input("股票代码", placeholder="例如：600000", value="600000")
    query_btn = st.button("查询", type="primary")

with col2:
    st.write("")

if query_btn or stock_code:
    if not stock_code:
        st.error("请输入股票代码")
    else:
        with st.spinner("正在获取数据..."):
            try:
                end_date = datetime.now().strftime('%Y%m%d')
                start_date = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')
                
                stock_df = ak.stock_zh_a_hist(
                    symbol=stock_code,
                    period="daily",
                    start_date=start_date,
                    end_date=end_date,
                    adjust="qfq"
                )
                
                if stock_df.empty:
                    st.error("未获取到数据，请检查股票代码")
                else:
                    st.success(f"✅ 成功获取 {stock_code} 的数据")
                    
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        fig = go.Figure(data=[go.Candlestick(
                            x=stock_df['日期'],
                            open=stock_df['开盘'],
                            high=stock_df['最高'],
                            low=stock_df['最低'],
                            close=stock_df['收盘'],
                            name='K线'
                        )])
                        
                        fig.update_layout(
                            title=f'{stock_code} K线图',
                            xaxis_title='日期',
                            yaxis_title='价格',
                            xaxis_rangeslider_visible=False,
                            height=600
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
                    
                    with col2:
                        st.subheader("数据统计")
                        latest = stock_df.iloc[0]
                        st.metric("最新收盘价", f"{latest['收盘']:.2f}")
                        st.metric("最高价", f"{latest['最高']:.2f}")
                        st.metric("最低价", f"{latest['最低']:.2f}")
                        st.metric("成交量", f"{latest['成交量']:,.0f}")
                    
                    st.subheader("原始数据")
                    st.dataframe(stock_df, use_container_width=True)
                    
                    csv = stock_df.to_csv(index=False, encoding='utf-8-sig')
                    st.download_button(
                        label="📥 下载CSV数据",
                        data=csv,
                        file_name=f'{stock_code}_stock_data.csv',
                        mime='text/csv'
                    )
                    
            except Exception as e:
                st.error(f"错误：{str(e)}")

st.markdown("---")
st.markdown("### 使用说明")
st.markdown("""
1. 输入A股股票代码（如：600000、000001等）
2. 点击"查询"按钮获取最近一年的K线数据
3. 查看K线图和数据统计
4. 可以下载CSV格式的原始数据
""")
