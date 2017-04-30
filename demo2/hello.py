import web
import time

urls = (
    "/", "index",
    "/sleep", "sleep",
    "/fib/(\d+)", "fib"
)
app = web.application(urls, globals())
application = app.wsgifunc()

class index:
    def GET(self):
        return "Hello, world!"

class sleep:
    def GET(self):
        i = web.input(t="1")
        t = float(i.t)
        time.sleep(t)
        return "good morning!\n"

class fib:
    def GET(self, n):
        n = int(n)
        value = self.fib(n)
        return str(value)

    def fib(self, n):
        if n < 2:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

if __name__ == "__main__":
    app.run()
