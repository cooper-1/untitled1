# -*-coding:  UTF-8
# @Time    :  2021/4/6 22:27
# @Author  :  Cooper
# @FileName:  test5.py
# @Software:  PyCharm
# !python3
import asyncio
import win32api, win32con  # moudle pywin32
import os
import aiohttp
import threading
import re
from pyppeteer import launch
from pyppeteer import launcher
from pyquery import PyQuery as pq

launcher.DEFAULT_ARGS.remove('--enable-automation')
# launcher.DEFAULT_ARGS.append('--disable-blink-features')
# launcher.DEFAULT_ARGS.append('--disable-blink-features=AutomationControlled')
# event_loop = asyncio.get_event_loop()
# aiohttp_session = aiohttp.ClientSession(loop=event_loop)
# 初始化操作


js = r"""delete navigator.webdriver;
var plugins = [
    {
        0: {
            "description": "Portable Document Format",
            "enabledPlugin": {},
            "suffixes": "pdf",
            "type": "application/x-google-chrome-pdf",
        },
        "description": "Portable Document Format",
        "filename": "internal-pdf-viewer",
        "length": 1,
        "name": "Chrome PDF Plugin",
    },
    {
        0: {
            "description": "",
            "enabledPlugin": {},
            "suffixes": "pdf",
            "type": "application/pdf",
        },
        "description": "",
        "filename": "mhjfbmdgcfjbbpaeojofohoefgiehjai",
        "length": 1,
        "name": "Chrome PDF Viewer",
    },
    {
        0: {
            "description": "Native Client Executable",
            "enabledPlugin": {},
            "suffixes": "",
            "type": "application/x-pnacl",
        },
        1: {
            "description": "Portable Native Client Executable",
            "enabledPlugin": {},
            "suffixes": "",
            "type": "application/x-nacl",
        },
        "description": "",
        "filename": "internal-nacl-plugin",
        "length": 2,
        "name": "Native Client",
    }
]


var dd = {
    "webdriver": undefined,
    "plugins": plugins,
    "languages": ['en-US', 'en'],
    "language": "en-US",
    "platform": "Win32",
};

for (var name in window.navigator) {
    if (name in dd) {
        Object.defineProperty(window.navigator, name, {
            value: dd[name],
        })
    }
}
delete navigator.webdriver;
let deviceInfo = {
            "window.speed":!window.speed?(typeof window.speed) : window.speed,
            "window.deviceorientation":!window.deviceorientation?(typeof window.deviceorientation):window.deviceorientation,
            "connectionInfo":connectionInfo(),
            "eval.toString().length":eval.toString().length,
            "'ontouchstart' in window":('ontouchstart' in window),
            "history" : {
                "history.length":history.length
            },
            "navigatorData": {
                "navigator.maxTouchPoints":1,
                "navigator.mimeTypes":navigator.mimeTypes.length,
                "navigator.vibrate":(typeof navigator.vibrate),
                "navigator.onLine":navigator.onLine,
                "navigator.userAgent": navigator.userAgent,
                "navigator.languages":navigator.languages,
                "navigator.language":navigator.language,
                "navigator.vendor":navigator.vendor,
                "navigator.appVersion":navigator.appVersion,
                "navigator.hardwareConcurrency":navigator.hardwareConcurrency,
                "navigator.devceMemory": !navigator.devceMemory ? "" : navigator.devceMemory,
                "navigator.appName":navigator.appName,
                "navigator.appCodeName":navigator.appCodeName,
                "navigator.cookieEnabled":navigator.cookieEnabled,
                "navigator.cpuClass": !navigator.cpuClass ? "" : navigator.cpuClass,
                "navigator.doNotTrack":(navigator.doNotTrack ? navigator.doNotTrack : navigator.msDoNotTrack ? navigator.msDoNotTrack : window.doNotTrack ? window.doNotTrack : undefined),
                "navigator.platform":navigator.platform,
                "navigator.product":navigator.product,
                "navigator.productSub":navigator.productSub,
                "navigator.vendorSub":navigator.vendorSub,
                "navigator.buildID":!navigator.buildID? "" : navigator.buildID,
                "navigator.connection":navigator.connection,
                "navigator.connection.effectiveType":navigator.connection ? navigator.connection.effectiveType : "",
                "navigator.plugins":navigator.plugins
            },
            "ClientTimezoneOffset":(new Date).getTimezoneOffset(),
            "window.chrome":!!window.chrome,
            "window.chrome.webstore": (!!window.chrome ? !!window.chrome.webstore : null),
            "window.CSS":!!window.CSS,
            "screenData": {
                "screen.width":screen.width,
                "screen.height":screen.height,
                "screen.availWidth":screen.availWidth,
                "screen.availHeight":screen.availHeight,
                "screen.colorDepth":screen.colorDepth,
                "screen.pixelDepth":screen.pixelDepth,
                "window.devicePixelRatio":window.devicePixelRatio,
                "screen.width * (window.devicePixelRatio || 1)":screen.width * (window.devicePixelRatio || 1),
                "screen.height * (window.devicePixelRatio || 1)":screen.height * (window.devicePixelRatio || 1)
            },
            "navigator.hardwareConcurrency":navigator.hardwareConcurrency,
            "webglInfo":webglInfo(),
            "adblockTest":adblockTest()
        }

        //console.log(JSON.stringify(deviceInfo));
        JSON.stringify(deviceInfo);



        navigator.getBattery().then(function(battery) {
            deviceInfo.batteryInfo = {
                "battery.level":battery.level,
                "battery.charging":battery.charging,
                "battery.dischargingTime":battery.dischargingTime
            }
            //document.writeln(JSON.stringify(deviceInfo));
        });

        function connectionInfo() {
                let nav = window.navigator;
                if (!nav.connection)
                    return "";
                var e = {};
                if (typeof nav.connection == "object") {
                    for (var t in nav.connection) {
                        if (typeof nav.connection[t] !== "function") {
                            e[t] = nav.connection[t];
                        }
                    }
                }
                return e;
        }

        function adblockTest() {
            var e = document.createElement("div");
            e.innerHTML = "&nbsp;",
            e.className = "adsbox";
            var t = !1;
            try {
                document.body && (document.body.appendChild(e),
                t = 0 === document.getElementsByClassName("adsbox")[0].offsetHeight,
                document.body.removeChild(e))
            } catch (n) {
                t = !1
            }
            return t
        }

        function webglInfo() {
            let canvasEle = document.createElement("canvas");
            let webglCtx = canvasEle.getContext("experimental-webgl");
            let webglDebugRenderInfo = webglCtx.getExtension("WEBGL_debug_renderer_info");
            let anisotropic = webglCtx.getExtension("EXT_texture_filter_anisotropic") || webglCtx.getExtension("WEBKIT_EXT_texture_filter_anisotropic") || webglCtx.getExtension("MOZ_EXT_texture_filter_anisotropic");
            let anisotropicExt = webglCtx.getParameter(anisotropic.MAX_TEXTURE_MAX_ANISOTROPY_EXT);
            let maxVertexTextureImageUnits = webglCtx.getShaderPrecisionFormat ? webglCtx.getShaderPrecisionFormat(webglCtx.VERTEX_SHADER, webglCtx.MEDIUM_FLOAT).precision : 0;
            let fragmentShaderBestPrecision = webglCtx.getShaderPrecisionFormat ? webglCtx.getShaderPrecisionFormat(webglCtx.FRAGMENT_SHADER, webglCtx.MEDIUM_FLOAT).precision : 0;
            let fragmentShaderFloatIntPrecision = (webglCtx.getShaderPrecisionFormat(webglCtx.FRAGMENT_SHADER, webglCtx.HIGH_FLOAT).precision ? "highp/" : "mediump/") + (webglCtx.getShaderPrecisionFormat(webglCtx.FRAGMENT_SHADER, webglCtx.HIGH_INT).rangeMax ? "highp" : "lowp")

            return {
                "RENDERER": webglCtx.getParameter(webglCtx.RENDERER),
                "VENDOR": webglCtx.getParameter(webglCtx.VENDOR),
                "VERSION": webglCtx.getParameter(webglCtx.VERSION),
                // 浏览器和手机一致不考虑
                "UNMASKED_RENDERER_WEBGL": webglCtx.getParameter(webglDebugRenderInfo.UNMASKED_RENDERER_WEBGL),
                "UNMASKED_VENDOR_WEBGL": webglCtx.getParameter(webglDebugRenderInfo.UNMASKED_VENDOR_WEBGL),
                "STENCIL_TEST": webglCtx.isEnabled(webglCtx.STENCIL_TEST),
                "SHADING_LANGUAGE_VERSION": webglCtx.getParameter(webglCtx.SHADING_LANGUAGE_VERSION),
                "RED_BITS": webglCtx.getParameter(webglCtx.RED_BITS),
                "GREEN_BITS": webglCtx.getParameter(webglCtx.GREEN_BITS),
                "BLUE_BITS": webglCtx.getParameter(webglCtx.BLUE_BITS),
                "ALPHA_BITS": webglCtx.getParameter(webglCtx.ALPHA_BITS),
                "MAX_RENDERBUFFER_SIZE": webglCtx.getParameter(webglCtx.MAX_RENDERBUFFER_SIZE),
                "MAX_COMBINED_TEXTURE_IMAGE_UNITS": webglCtx.getParameter(webglCtx.MAX_COMBINED_TEXTURE_IMAGE_UNITS),
                "MAX_CUBE_MAP_TEXTURE_SIZE": webglCtx.getParameter(webglCtx.MAX_CUBE_MAP_TEXTURE_SIZE),
                "MAX_FRAGMENT_UNIFORM_VECTORS": webglCtx.getParameter(webglCtx.MAX_FRAGMENT_UNIFORM_VECTORS),
                "MAX_TEXTURE_IMAGE_UNITS": webglCtx.getParameter(webglCtx.MAX_TEXTURE_IMAGE_UNITS),
                "MAX_TEXTURE_SIZE": webglCtx.getParameter(webglCtx.MAX_TEXTURE_SIZE),
                "MAX_VARYING_VECTORS": webglCtx.getParameter(webglCtx.MAX_VARYING_VECTORS),
                "MAX_VERTEX_ATTRIBS": webglCtx.getParameter(webglCtx.MAX_VERTEX_ATTRIBS),
                "MAX_VERTEX_UNIFORM_VECTORS": webglCtx.getParameter(webglCtx.MAX_VERTEX_UNIFORM_VECTORS),
                "ALIASED_LINE_WIDTH_RANGE": webglCtx.getParameter(webglCtx.ALIASED_LINE_WIDTH_RANGE),
                "ALIASED_POINT_SIZE_RANGE": webglCtx.getParameter(webglCtx.ALIASED_POINT_SIZE_RANGE),
                "MAX_VIEWPORT_DIMS": webglCtx.getParameter(webglCtx.MAX_VIEWPORT_DIMS),
                //t.getParameter(n.MAX_DRAW_BUFFERS_WEBGL) // 手机也返回null
                "anisotropicExt": anisotropicExt,
                "maxVertexTextureImageUnits": maxVertexTextureImageUnits,
                "MAX_VERTEX_TEXTURE_IMAGE_UNITS": webglCtx.getParameter(webglCtx.MAX_VERTEX_TEXTURE_IMAGE_UNITS),
                "fragmentShaderBestPrecision": fragmentShaderBestPrecision,
                "DEPTH_BITS": webglCtx.getParameter(webglCtx.DEPTH_BITS),
                "STENCIL_BITS": webglCtx.getParameter(webglCtx.STENCIL_BITS),
                "getSupportedExtensions": webglCtx.getSupportedExtensions(),
                "fragmentShaderFloatIntPrecision": fragmentShaderFloatIntPrecision
            };
        }
webglInfo();
"""
# ['zh-CN', 'zh', 'en']
# brower=None
# 此处设置代理
proxy = None
# getScreenSize
width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)


# 绕过检测
async def setOnePage(brower):
    pages = await brower.pages()
    page = pages[0]
    await page.evaluateOnNewDocument('''() =>{Object.defineProperty(navigator, 'webdriver', {get: () => undefined})}''')
    await page.evaluateOnNewDocument('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluateOnNewDocument(
        '''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluateOnNewDocument(
        '''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')


# 创建浏览器函数
async def init():
    global brower
    global width
    global height
    brower = await launch({
        'ignoreHTTpSErrors': True,  # （布尔）：是否忽略HTTPS错误。默认为 False。
        'headless': True,  # （布尔）：是否以无头模式运行浏览器。默认为， True除非appMode或devtools选项为True。
        'executablePath': r"D:\chrome-win32\chrome.exe",  # （str）：运行而不是默认捆绑的Chromium的Chromium或Chrome可执行文件的路径。
        # 'slowMo':,#（int | float）：将pyppeteer操作减慢指定的毫秒数。
        'args': [
            '--start-maximized',  # 设置浏览器窗口大小，保持和页面大小一致
            '--no-sandbox',
            '--disable-infobars',
            '--ignore-certificate-errors',
            '--enable-extensions',
            '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
            # '--disable-gpu',
            # '--disable-suggestions-ui',
            # --proxy-server=127.0.0.1:1080 # 使用代理
        ],  # （List [str]）：传递给浏览器进程的其他参数（标志）
        # 'ignoreDefaultArgs':True,#（布尔）：不使用pyppeteer的默认参数。这是危险的选择。小心使用
        # 'handleSIGINT':,#（布尔）：在Ctrl + C上关闭浏览器进程。默认为 True。
        # 'handleSIGTERM':,#（布尔）：关闭SIGTERM上的浏览器进程。默认为True。
        # 'handleSIGHUP':,#（布尔）：关闭SIGHUP上的浏览器进程。默认为 True。
        'dumpio': True,  # （布尔）：是否将浏览器进程stdout和stderr用管道传输到process.stdout和中process.stderr。默认为False。
        'userDataDir': r'D:\userData',  # （str）：用户数据目录的路径。
        # 'env':,#（字典）：指定对浏览器可见的环境变量。默认与python进程相同。
        # 'devtools':,#（布尔）：是否为每个选项卡自动打开DevTools面板。如果是此选项True，headless则将设置该选项 False。
        # 'logLevel':,#（int | str）：日志级别以打印日志。默认与根记录器相同。
        'autoClose': True,  # （布尔）：脚本完成后自动关闭浏览器进程。默认为True。
        # 'loop':,#（asyncio.AbstractEventLoop）：事件循环（实验性）。
    })
    # print("默认Use-Agent",brower.userAgent())
    # await setOnePage(brower)


# 修改浏览器设置
async def swapproxy_js(request):
    global proxy

    js_1 = """Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
window.navigator.chrome = { runtime: {},  };
Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], });"""
    # js=''
    # 构造请求添加代理
    req = {
        "headers": request.headers,
        "data": request.postData,
        "proxy": proxy,
        "timeout": 5,
        "ssl": False,
    }
    try:
        # 使用第三方库获取响应
        async with aiohttp_session.request(
                method=request.method, url=request.url, **req
        ) as response:
            body = await response.read()
    except Exception as e:
        await request.abort()
        return
    # js注入
    body = body.replace(b"<title>", b"<script>%s</script><title>" % js.encode())
    # 返回数据给浏览器
    respond = {"body": body, "headers": response.headers, "status": response.status}
    await request.respond(respond)
    return


# 修改浏览器属性1
async def change_status(page):
    # await page.evaluate('''() =>{ Object.defineProperty(navigator, 'webdriver', {get: () => undefined}); }''')
    # await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    # await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    # await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')
    await page.evaluateOnNewDocument(
        '''() =>{ Object.defineProperty(navigator, 'webdriver', {get: () => undefined});}''')
    await page.evaluateOnNewDocument('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluateOnNewDocument(
        '''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    # await page.evaluateOnNewDocument('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')
    await page.evaluateOnNewDocument('''() =>{ delete navigator.__proto__.webdriver }''')
    await page.evaluateOnNewDocument('() =>{' + js + '}')
    # await page.addScriptToEvaluateOnNewDocument('''() =>{ Object.defineProperty(navigator, 'webdriver', {get: () => undefined});}''')
    # await page.addScriptToEvaluateOnNewDocument('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    # await page.addScriptToEvaluateOnNewDocument('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    # await page.addScriptToEvaluateOnNewDocument('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')


# 爬取页面
async def crawl(url):
    global brower
    global width
    global height
    page = await brower.newPage()
    page.setDefaultNavigationTimeout(10 * 1000)
    await page.setViewport(viewport={'width': width, 'height': height})  #
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
    # await page.setRequestInterception(True)
    # page.on('request',swapproxy_js)
    await change_status(page)
    try:
        await page.goto(url)
    except:
        pass
    # await page.evaluate('window.scrollBy(0, window.innerHeight)')#滚动到底部fail
    await asyncio.sleep(1)
    js_pnt = r"""function alertObj(obj){
    var str="";
    for (var item in obj){
        str +=item+":"+obj[item]+"\n";
    }
    document.writeln("<p><pre/>"+str);
    document.writeln("</pre></p>");
}

alertObj(navigator);"""
    # await page.evaluate('() =>{'+js_pnt+'}')
    await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')  # 滚动到底部
    content = await page.content()
    doc = pq(content)

    fname = url + '+' + doc('title').text()
    fname = fname.translate(str.maketrans('', '', r'/\|*<>":?'))
    fname = fname.replace('https', '')
    fname = fname.replace('http', '')
    file = open(fname + '.html', 'wb')
    file.write(content.encode())
    file.close
    await page.emulateMedia('screen')
    await page.screenshot({'path': fname + '.png', 'fullPage': True})
    # await page.pdf({'path': fname+'.pdf','printBackground':True})

    # await page.close()


class ccrawl(threading.Thread):  # class crawl
    def __init__(self, sites):
        threading.Thread.__init__(self)
        self.sites = sites

    async def initbrower(self, headless):
        self.debug = headless
        brower = await launch({
            'ignoreHTTpSErrors': True,  # （布尔）：是否忽略HTTPS错误。默认为 False。
            'headless': headless,  # （布尔）：是否以无头模式运行浏览器。默认为， True除非appMode或devtools选项为True。
            'executablePath': r"D:\Software\SystemTool\MyChrome_x64\App\chrome.exe",
            # （str）：运行而不是默认捆绑的Chromium的Chromium或Chrome可执行文件的路径。
            # 'slowMo':,#（int | float）：将pyppeteer操作减慢指定的毫秒数。
            'args': [
                '--start-maximized',  # 设置浏览器窗口大小，保持和页面大小一致
                '--no-sandbox',
                '--disable-infobars',
                '--ignore-certificate-errors',
                '--enable-extensions',
                '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
                # '--disable-gpu',
                # '--disable-suggestions-ui',
                # --proxy-server=127.0.0.1:1080 # 使用代理
            ],  # （List [str]）：传递给浏览器进程的其他参数（标志）
            # 'ignoreDefaultArgs':True,#（布尔）：不使用pyppeteer的默认参数。这是危险的选择。小心使用
            # 'handleSIGINT':,#（布尔）：在Ctrl + C上关闭浏览器进程。默认为 True。
            # 'handleSIGTERM':,#（布尔）：关闭SIGTERM上的浏览器进程。默认为True。
            # 'handleSIGHUP':,#（布尔）：关闭SIGHUP上的浏览器进程。默认为 True。
            'dumpio': True,  # （布尔）：是否将浏览器进程stdout和stderr用管道传输到process.stdout和中process.stderr。默认为False。
            'userDataDir': r'D:\userData',  # （str）：用户数据目录的路径。
            # 'env':,#（字典）：指定对浏览器可见的环境变量。默认与python进程相同。
            # 'devtools':,#（布尔）：是否为每个选项卡自动打开DevTools面板。如果是此选项True，headless则将设置该选项 False。
            # 'logLevel':,#（int | str）：日志级别以打印日志。默认与根记录器相同。
            'autoClose': True,  # （布尔）：脚本完成后自动关闭浏览器进程。默认为True。
            # 'loop':,#（asyncio.AbstractEventLoop）：事件循环（实验性）。
        })
        self.brower = brower

    async def simulation(self, page):
        await page.evaluateOnNewDocument("""let mimeTypes = [{
    "description": "",
    "enabledPlugin": {},
    "suffixes": "pdf",
    "type": "application/pdf"
}, {
    "description": "Portable Document Format",
    "enabledPlugin": {},
    "suffixes": "pdf",
    "type": "application/x-google-chrome-pdf"
}, {
    "description": "Native Client Executable",
    "enabledPlugin": {},
    "suffixes": "",
    "type": "application/x-nacl"
}, {
    "description": "Portable Native Client Executable",
    "enabledPlugin": {},
    "suffixes": "",
    "type": "application/x-pnacl"
}];

const makeFnsNative = (fns = []) => {
          const oldCall = Function.prototype.call
          function call () {
            return oldCall.apply(this, arguments)
          }
          // eslint-disable-next-line
          Function.prototype.call = call

          const nativeToStringFunctionString = Error.toString().replace(
            /Error/g,
            'toString'
          )
          const oldToString = Function.prototype.toString

          function functionToString () {
            for (const fn of fns) {
              if (this === fn.ref) {
                return `function ${fn.name}() { [native code] }`
              }
            }

            if (this === functionToString) {
              return nativeToStringFunctionString
            }
            return oldCall.call(oldToString, this)
          }
          // eslint-disable-next-line
          Function.prototype.toString = functionToString
        }
Object.defineProperty(navigator, 'plugins', {
    get: () => pluginArray
  })""")

        """//mimeTypes.map(o => Object.setPrototypeOf(o,MimeType.prototype));
    //Object.setPrototypeOf(mimeTypes,MimeTypeArray.prototype);
    //navigator.plugins.__proto__
    
    //PluginArray {item: ƒ, namedItem: ƒ, refresh: ƒ, constructor: ƒ, …}
    //length: (...)
    //item: ƒ item()
    //namedItem: ƒ namedItem()
    //refresh: ƒ refresh()
    //navigator.mimeTypes.__proto__
    
    //MimeTypeArray {Symbol(Symbol.toStringTag): "MimeTypeArray", item: ƒ, namedItem: ƒ, constructor: ƒ, …}
    //length: (...)
    //item: ƒ item()
    //namedItem: ƒ namedItem()
    //navigator.plugins.item.toString();
    //"function item() { [native code] }"""

    async def rm(self, page):
        # rm webdriver
        await page.evaluateOnNewDocument("""() => {
    const newProto = navigator.__proto__;
    delete newProto.webdriver;
    navigator.__proto__ = newProto;
  }""")
        await page.evaluateOnNewDocument("""() => {
    window.navigator.chrome = {
        runtime: {}
      };
  }""");
        with open(r'd:\stealth.min.js') as res:
            tmpjs = res.read()
            await page.evaluateOnNewDocument(tmpjs)

    async def curl(self, url):
        brower = self.brower
        page = await brower.newPage()
        page.setDefaultNavigationTimeout(10 * 1000)

        await page.setViewport(viewport={'width': width, 'height': height})  #
        await page.setJavaScriptEnabled(enabled=True)
        await page.setUserAgent(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
        # await page.setRequestInterception(True)
        # page.on('request',swapproxy_js)
        # await self.simulation(page)
        # await self.rm(page)
        # await change_status(page)
        # await page.evaluateOnNewDocument(self.stealth_min_js)
        with open(r'd:\stealth.min.js') as res:
            tmpjs = res.read()
        await page.evaluateOnNewDocument('() =>{ ' + tmpjs + ' }')
        try:
            await page.goto(url)
        except:
            pass
        # await page.evaluate('window.scrollBy(0, window.innerHeight)')#滚动到底部fail
        await asyncio.sleep(1)
        js_pnt = r"""function alertObj(obj){
        var str="";
        for (var item in obj){
            str +=item+":"+obj[item]+"\n";
        }
        document.writeln("<p><pre/>"+str);
        document.writeln("</pre></p>");
    }

    alertObj(navigator);"""
        # await page.evaluate('() =>{'+js_pnt+'}')
        await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')  # 滚动到底部
        content = await page.content()
        doc = pq(content)

        fname = url + '+' + doc('title').text()
        fname = fname.translate(str.maketrans('', '', r'/\|*<>":?'))
        fname = fname.replace('https', '')
        fname = fname.replace('http', '')
        file = open(fname + '.html', 'wb')
        file.write(content.encode())
        file.close
        await page.emulateMedia('screen')
        await page.screenshot({'path': fname + '.png', 'fullPage': True})
        if self.debug:
            await page.pdf({'path': fname + '.pdf', 'printBackground': True})

    async def csite(self, onesite):
        await curl(onesite)


def mtd(url):  # multithreading
    crawl(url)


# http://www.nhc.gov.cn/xcs/yqfkdt/202101/b646a63a57854c8aabbbe344f0a0aebb.shtml
# http://quotes.toscrape.com/js/
# https://bot.sannysoft.com/
async def main1():
    # await init()
    # await crawl('https://bot.sannysoft.com/')

    sites = ['https://bot.sannysoft.com/']
    test = ccrawl(sites)
    await test.initbrower(True)
    await test.curl('https://bot.sannysoft.com/')
    input()


# if __name__ == '__main__':
# event_loop.run_until_complete(main())

# 代码重构
import threading
import time


# 创建类
async def test111(request):
    # 构造请求并添加代理
    req = {
        "headers": request.headers,
        "data": request.postData,
        "proxy": None,  # 使用全局变量 则可随意切换
        "timeout": 5,
        "ssl": False,
    }
    try:
        # 使用第三方库获取响应
        async with aiohttp_session.request(
                method=request.method, url=request.url, **req
        ) as response:
            body = await response.read()
    except Exception as e:
        await request.abort()
        return

    # 数据返回给浏览器
    resp = {"body": body, "headers": response.headers, "status": response.status}
    await request.respond(resp)
    return


class crawl:

    async def __initbrower(self):

        self.brower = await launch({
            'ignoreHTTpSErrors': True,  # （布尔）：是否忽略HTTPS错误。默认为 False。
            'headless': ~self.debug,  # （布尔）：是否以无头模式运行浏览器。默认为， True除非appMode或devtools选项为True。
            # 'executablePath':r"D:\Software\SystemTool\MyChrome_x64\App\chrome.exe",#（str）：运行而不是默认捆绑的Chromium的Chromium或Chrome可执行文件的路径。
            'executablePath': r"D:\chrome-win32\chrome.exe",
            # 'slowMo':,#（int | float）：将pyppeteer操作减慢指定的毫秒数。
            'args': [
                '--start-maximized',  # 设置浏览器窗口大小，保持和页面大小一致
                '--no-sandbox',
                '--disable-infobars',
                '--ignore-certificate-errors',
                '--enable-extensions',
                '--window-size=1920,1080',
                '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
                # '--disable-gpu',
                # '--disable-suggestions-ui',
                # --proxy-server=127.0.0.1:1080 # 使用代理
            ],  # （List [str]）：传递给浏览器进程的其他参数（标志）
            # 'ignoreDefaultArgs':True,#（布尔）：不使用pyppeteer的默认参数。这是危险的选择。小心使用
            # 'handleSIGINT':,#（布尔）：在Ctrl + C上关闭浏览器进程。默认为 True。
            # 'handleSIGTERM':,#（布尔）：关闭SIGTERM上的浏览器进程。默认为True。
            # 'handleSIGHUP':,#（布尔）：关闭SIGHUP上的浏览器进程。默认为 True。
            'dumpio': True,  # （布尔）：是否将浏览器进程stdout和stderr用管道传输到process.stdout和中process.stderr。默认为False。
            'userDataDir': 'D:/pyppeteer_ChromeuserData',  # （str）：用户数据目录的路径。
            # 'env':,#（字典）：指定对浏览器可见的环境变量。默认与python进程相同。
            # 'devtools':,#（布尔）：是否为每个选项卡自动打开DevTools面板。如果是此选项True，headless则将设置该选项 False。
            # 'logLevel':,#（int | str）：日志级别以打印日志。默认与根记录器相同。
            'autoClose': True,  # （布尔）：脚本完成后自动关闭浏览器进程。默认为True。
            # 'loop':,#（asyncio.AbstractEventLoop）：事件循环（实验性）。
        })

    def __init__(self, debug=False):  # ,*,url,sites):
        self.cdp = True
        self.debug = debug
        self.url = None  # url
        self.proxy = None
        event_loop = asyncio.get_event_loop()
        self.loop = event_loop
        if debug is True:
            self.debug = debug

        event_loop.run_until_complete(self.__initbrower())

    async def swap_proxy_js(self, request):
        aiohttp_session = aiohttp.ClientSession(loop=event_loop)
        req = {
            "headers": request.headers,
            "data": request.postData,
            "proxy": self.proxy,  # 使用全局变量 则可随意切换
            "timeout": 5,
            "ssl": False,
        }
        try:
            # 使用第三方库获取响应
            async with aiohttp_session.request(
                    method=request.method, url=request.url, **req
            ) as response:
                body = await response.read()
        except Exception as e:
            await request.abort()
            return

        if self.cdp == False:
            with open("pass_webdriver.js") as f:
                js = f.read()
            # 在html源码头部添加js代码 修改navigator属性
            body = body.replace(b"<title>", b"<script>%s</script><title>" % js.encode())

        # 数据返回给浏览器
        resp = {"body": body, "headers": response.headers, "status": response.status}
        print(resp)
        print(1)
        await request.respond(resp)
        return

    async def curl(self, url):
        page = await self.brower.newPage()
        page.setDefaultNavigationTimeout(10 * 1000)
        await page.setViewport(viewport={'width': width, 'height': height})  #
        await page.setJavaScriptEnabled(enabled=True)
        await page.setRequestInterception(True)
        page.on('request', swapproxy_js)
        try:
            await page.goto(url)
        except:
            pass
        await asyncio.sleep(1)
        await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')  # 滚动到底部
        content = await page.content()
        doc = pq(content)

        fname = url + '+' + doc('title').text()
        fname = fname.translate(str.maketrans('', '', r'/\|*<>":?'))
        fname = fname.replace('https', '')
        fname = fname.replace('http', '')
        file = open(fname + '.html', 'wb')
        file.write(content.encode())
        file.close
        await page.emulateMedia('screen')
        await page.screenshot({'path': fname + '.png', 'fullPage': True})
        if self.debug:
            await page.pdf({'path': fname + '.pdf', 'printBackground': True})

    def run(self, hs):
        self.loop.run_until_complete(hs)


# 最后亿次重构
event_loop = asyncio.get_event_loop()
height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)


async def initbrower(width, height):
    return await launch({
        'ignoreHTTpSErrors': False,  # （布尔）：是否忽略HTTPS错误。默认为 False。
        'headless': False,  # （布尔）：是否以无头模式运行浏览器。默认为， True除非appMode或devtools选项为True。
        'executablePath': "./Chrome/Chrome.exe",  # （str）：运行而不是默认捆绑的Chromium的Chromium或Chrome可执行文件的路径。
        # 'slowMo':,#（int | float）：将pyppeteer操作减慢指定的毫秒数。
        'args': [
            '--start-maximized',  # 设置浏览器窗口大小，保持和页面大小一致
            '--disable-infobars',
            '--ignore-certificate-errors',
            '--enable-extensions',
            '--window-size=' + str(height) + ',' + str(width),
            '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        ],  # （List [str]）：传递给浏览器进程的其他参数（标志）
        # 'ignoreDefaultArgs':True,#（布尔）：不使用pyppeteer的默认参数。这是危险的选择。小心使用
        # 'handleSIGINT':,#（布尔）：在Ctrl + C上关闭浏览器进程。默认为 True。
        # 'handleSIGTERM':,#（布尔）：关闭SIGTERM上的浏览器进程。默认为True。
        # 'handleSIGHUP':,#（布尔）：关闭SIGHUP上的浏览器进程。默认为 True。
        'dumpio': True,  # （布尔）：是否将浏览器进程stdout和stderr用管道传输到process.stdout和中process.stderr。默认为False。
        'userDataDir': './pyppeteer_ChromeuserData',  # （str）：用户数据目录的路径。
        # 'env':,#（字典）：指定对浏览器可见的环境变量。默认与python进程相同。
        # 'devtools':,#（布尔）：是否为每个选项卡自动打开DevTools面板。如果是此选项True，headless则将设置该选项 False。
        # 'logLevel':,#（int | str）：日志级别以打印日志。默认与根记录器相同。
        'autoClose': True,  # （布尔）：脚本完成后自动关闭浏览器进程。默认为True。
        # 'loop':,#（asyncio.AbstractEventLoop）：事件循环（实验性）。
    })


class crawl:
    brower = None
    url = None
    sub = []
    source = []
    depth = 0
    domain = None

    def getdomain(self, url):
        url = url + '/'
        domain = re.match('https?://.+?\\..+?/+?', url, re.I)
        if domain is not None:
            tmp = domain.span()
            Str = ''.join(list(url)[:tmp[1]])
            print(Str)
            return Str
        else:
            print('please input correct format:http(s):xxxxxxxxxxx')
            exit()

    def getmurl(self, content):  # 获取所有可能的url Get May Url
        murl1 = re.findall(".*\'(.*?)\'", content)
        # print('content:',content)
        # print(murl1)
        murl2 = re.findall("\"(.*?)\"", content)
        return murl1 + murl2

    def getturl(self, murl):  # 获取正确的url Get True Url
        surl = []
        dot = '[^ $;]'
        for i in murl:
            if re.match('//[^ $;]*?', i, re.I) is not None:
                i = 'http' + i
                surl.append(i)
            elif re.match('/[^ $;]+/', i, re.I) is not None:
                i = crawl.domain + i
                surl.append(i)
            elif re.match('/[^ $;]*?\\.[^ :$;]*', i, re.I) is not None:
                i = crawl.domain + i
                surl.append(i)
            elif re.match('[^ $;.]+\\.[^ $;.]+\\.[^ $;]*?', i, re.I) is not None:
                surl.append(i)
            elif re.match('./[^ $;]*?/[^ $;]*?', i, re.I) is not None:
                i = crawl.domain + i
                surl.append(i)
            elif re.match('http.+?.?/?', i, re.I) is not None:
                surl.append(i)
            else:
                pass
        surl = list(set(surl))
        return surl

    async def geturl(self, url):
        page = await crawl.brower.newPage()
        await page.setViewport(viewport={'width': width, 'height': height})
        await page.setJavaScriptEnabled(enabled=True)
        # await rm(page)
        try:
            await page.goto(url)
        except:
            pass
        # await asyncio.sleep(1)
        await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')  # 滚动到底部
        content = await page.content()
        '''doc = pq(content)
    
        fname = url+'+'+doc('title').text()
        fname = fname.translate(str.maketrans('','',r'/\|*<>":?'))
        fname = fname.replace('https','')
        fname = fname.replace('http','')
        file = open(fname+'.html','wb')
        file.write(content.encode())
        file.close
        await page.emulateMedia('screen')
        await page.screenshot({'path': fname+'.png','fullPage':True})
        if self.debug:
          await page.pdf({'path': fname+'.pdf','printBackground':True})'''
        return content

    async def getsurl(self):  # 获取子url Get Sub Url
        content = await self.geturl(crawl.url)
        murl = self.getmurl(content)
        # print(murl)
        turl = self.getturl(murl)
        self.sub = turl
        self.source.append(crawl.url)
        print(turl)

    async def getsite(self, url, depth):
        self.geturl

    def setdepth(self, depth):
        crawl.depth = depth

    def __init__(self, brower, url):
        crawl.brower = brower
        crawl.url = url
        crawl.domain = self.getdomain(url)

    async ret(self, depth):


async def test1():
    brower = await initbrower(width, height)
    url = 'https://baidu.com'
    test1 = crawl(brower, url)
    await test1.getsurl()


if __name__ == '__main__':
    event_loop.run_until_complete(test1())
