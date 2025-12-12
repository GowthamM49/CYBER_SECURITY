import streamlit as st
from scapy.all import rdpcap, TCP, IP, UDP
import tempfile
import pandas as pd
from collections import Counter

st.set_page_config(page_title="WireShark",layout="wide")

st.title("Network packet Analyzer ")
st.write("Please upload the pcap file (.pcap/.pcapng)")

uploaded_file=st.file_uploader("Choose a pcap file",type=["pcap"])
# lets design packects functions
def load_packets(file_bytes):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file_bytes)
        temp_path = temp_file.name
    packets = rdpcap(temp_path)
    return packets  
def analyxe_packets(packets):
    total_packets=len(packets)
    protocal_count=Counter()




    
