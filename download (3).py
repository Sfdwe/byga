class Smartphone:
    # Атрибуты класса
    os = "Android"
    manufacturer = "Samsung"

    def __init__(
        self, 
        model: str, 
        storage: int, 
        ram: int, 
        camera_mp: float, 
        battery_capacity: int
    ) -> None:
        """Инициализация объекта смартфона"""
        # Атрибуты объекта
        self.model = model
        self.storage = storage  # в ГБ
        self.ram = ram  # в ГБ
        self.camera_mp = camera_mp  # мегапиксели
        self.battery_capacity = battery_capacity  # в mAh
        self.is_on = False

    def __str__(self) -> str:
        """Строковое представление объекта"""
        return (f"{self.manufacturer} {self.model} ({self.os}), "
                f"{self.storage}GB/{self.ram}GB, "
                f"{self.camera_mp}MP camera, "
                f"{self.battery_capacity}mAh")

    def power_on(self) -> None:
        """Включить смартфон"""
        if not self.is_on:
            self.is_on = True
            print(f"{self.model} включен")
        else:
            print(f"{self.model} уже включен")

    def power_off(self) -> None:
        """Выключить смартфон"""
        if self.is_on:
            self.is_on = False
            print(f"{self.model} выключен")
        else:
            print(f"{self.model} уже выключен")

    def take_photo(self) -> str:
        """Сделать фото"""
        if self.is_on:
            return f"Сделано фото на {self.camera_mp}MP камеру"
        return "Сначала включите смартфон"

    def check_storage(self, app_size: float) -> bool:
        """Проверить, хватит ли места для приложения"""
        return app_size <= self.storage * 0.8  # Оставляем 20% свободного места

    @classmethod
    def change_os(cls, new_os: str) -> None:
        """Изменить ОС для всех смартфонов"""
        cls.os = new_os


# Создание объектов
phone1 = Smartphone("Galaxy S23", 256, 8, 50.0, 3900)
phone2 = Smartphone("Galaxy A54", 128, 6, 32.5, 5000)

# Использование методов
print(phone1)
print(phone2)

phone1.power_on()
print(phone1.take_photo())

phone2.power_on()
print(phone2.check_storage(15.5))

Smartphone.change_os("Android 14")
print(f"Новая ОС всех смартфонов: {Smartphone.os}")
