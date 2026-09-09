class Phone:

    def __init__(
        self,
        brand,
        model,
        price,
        processor=None,
        display=None,
        camera=None,
        battery=None,
        ram=None,
        storage=None,
        ratings=None
    ):

        self.brand = brand

        self.model = model

        self.full_name = (
            f"{brand} {model}"
        )

        self.price = price

        self.processor = processor

        self.display = display

        self.camera = camera

        self.battery = battery

        self.ram = ram

        self.storage = storage

        self.ratings = ratings or {}


    def to_dict(self):

        return {

            "brand":
                self.brand,

            "model":
                self.model,

            "full_name":
                self.full_name,

            "price":
                self.price,

            "processor":
                self.processor,

            "display":
                self.display,

            "camera":
                self.camera,

            "battery":
                self.battery,

            "ram":
                self.ram,

            "storage":
                self.storage,

            "ratings":
                self.ratings

        }