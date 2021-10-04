from service.IOCContainer import IOCContainer


if __name__ == "__main__":
    app = IOCContainer().get_webserver()
    app.run()

