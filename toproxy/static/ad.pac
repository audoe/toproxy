// http://pac.itzmx.com

var proxy = "PROXY 183.57.76.181:8109;";

var domains = {
  "lf.snssdk.com":1,
  "mi.gdt.qq.com":1,
  "c.3g.163.com":1,
  "g1.163.com":1,
  "r.cnews.qq.com":1,
  "news.l.qq.com":1,
  "c.m.163.com":1,
  "zyzc9.com": 1
};

var direct = 'DIRECT;';

var hasOwnProperty = Object.hasOwnProperty;

function FindProxyForURL(url, host) {
    if (host == "www.haosou.com") {
        return "PROXY 360.itzmx.com:80";
    }

    var suffix;
    var pos = host.lastIndexOf('.');
    while(1) {
        suffix = host.substring(pos + 1);
        if (hasOwnProperty.call(domains, suffix)) {
            return proxy;
        }
        if (pos <= 0) {
            break;
        }
        pos = host.lastIndexOf('.', pos - 1);
    }
    return direct;
}