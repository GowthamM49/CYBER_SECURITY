import streamlit as st
import re

def check_strength(password):
    score=0
    suggestions=[]
    if len(password)>=8:
        score+=1
    else:
        suggestions.append("Use at least 8 characters.")
    if re.search("[A-z]", password):
        score+=1
    else:
        suggestions.append("Include at least one letter.")
    if re.search("[a-z]", password):
        score+=1
    else:
        suggestions.append("Include at least one lowercase letter.")
    if re.search("[0-9]", password):
        score+=1
    else:
        suggestions.append("Include at least one digit.")
    if re.search("[@#$%^&+=]", password):
        score+=1    
    else:
        suggestions.append("Include at least one special character (@#$%^&+=).")
    return score, suggestions
# main()
st.title("Password Strength Checker: ")
st.write("Enter a password to check How Strong it is")
password = st.text_input("Enter your password:",type="password")
if password:
    score, suggestions = check_strength(password)
    st.progress(score/5)
    strength_levels = ["very weak", "weak", "moderate", "strong", "Excellent"]
    st.subheader(f"Strength: {strength_levels[score-1]}")
    if suggestions:
        st.subheader("Suggestions to improve your password:")
        for s in suggestions:
            st.write(f"- {s}")
    else:
        st.success("Your password is strong!")
    