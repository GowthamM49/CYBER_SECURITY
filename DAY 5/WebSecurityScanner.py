import streamlit as st
import requests
import ssl

st.set_page_config(page_title="Web Security Scanner", layout="wide")
st.title("WEB SECURITY SCANNER")
st.write("Enetr the URL to check for scanning common issues.")
url=st.text_input("Enter URL (Ex: https://example.com)")

sql_payloads = ["'", "\"", "' OR 1=1--", "\" OR 1=1--", "';", "' OR '1'='1"]


def test_sql_injection(base_url):
    results=[]
    for i in sql_payloads:
        try:
            test_url=base_url+i
            res=requests.get(test_url, timeout=5)
            errors=["mysql","syntax error","sql error","warning","Unclosed quotes"]

        except:
            pass
    return results if results else ["No SQL Injection symptoms detected."]

xss_payloads = [
    "<script>alert('XSS');</script>",
    "<script>alert(document.cookie);</script>",
    "<img src=x onerror=alert('XSS')>"
    ]


def test_xss(base_url):
    results=[]
    for payload in xss_payloads:
        try:
            test_url=base_url+payload
            res=requests.get(test_url, timeout=5)
            if payload in res.text:
                results.append(f"Possible payload found: {payload}") 
        except:
            pass
    return results if results else ["No XSS symptoms detected."]
required=[
    "Content-Security-Policy",
    "Xss-Protection",
    "X-Frame-Policy",
    "Strict-Transport-Security"
]

def check_headers(base_url):
    missing=[]
    try:
        res=requests.get(base_url, timeout=5)
        headers=res.headers
        for h in check_headers:
            if h not in headers:
                missing.append(f"Missing security header: {h}")
    except:
        return ["Unable to fetch headers."]
    return missing if missing else ["All essential security headers are present."]

def check_https(base_url):
    if base_url.startswith("https://"):
        return "HTTPS is enabled."
    else:
        return "Website is not using HTTPS."
    
comman_path=[
    "/login","/config","/test","/admin","/dev","/backup","/server-status","/dashboard"
]
def scan_directories(base_url):
    found=[]
    for path in comman_path:
        try:
            test_url=base_url+path
            res=requests.get(test_url,timeout=5)
            if res.status_code==200:
                found.append(f"Accessible sensitive endpoint: {test_url}")
        except:
            pass
    return found if found else "No Exposed Sensitive directories."

if st.button("Scan Website"):
    if not url:
        st.error("Please enter a valid URL.")
    else:
        st.markdown("### Running Security Tests")

        st.subheader("1. SQL Injection Test")
        sql_results=test_sql_injection(url)

        for r in sql_results:
            st.write(r)

        st.subheader("2. XSS Test")
        xss_results=test_xss(url)
        for r in xss_results:
            st.write(r)

        st.subheader("3. Security Headers Check")

        