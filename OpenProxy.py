import re
import pandas as pd

ProxyListSite = "https://www.proxynova.com/proxy-server-list/"
class OpenProxy():
    def GetOpenProxyList(self):
        dfs = pd.read_html(ProxyListSite, header=0)
        ret = []
        for (ip_raw, port) in dfs[0][["Proxy IP","Proxy Port"]].values.tolist():
            if type(ip_raw) == str:
                ip = re.search("document.write\('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\'\)", ip_raw)
                if ip != None:
                    ret.append("http://" + ip.group(1) + ":" + port)

        return ret


if __name__ == '__main__':
    op = OpenProxy()
    print(op.GetOpenProxyList())

