# GameConfig.py
import json
import os
from typing import Dict, Any

class GameConfig:
    """Класс конфигурации игры с использованием @property и сохранением в JSON"""
    
    def __init__(self, config_file="game_config.json"):
        self._config_file = config_file
        self._game_title = "Стратегическая Игра"
        self._max_players = 2
        self._starting_resources = 1000
        self._map_size = (10, 10)
        self._difficulty = "normal"
        self._game_version = "1.0"
        self._auto_save = True
        self._music_volume = 80
        self._sound_volume = 90
        
        # Загружаем конфигурацию при создании объекта
        self.load_from_file()
    
    # === Свойства с использованием @property ===
    
    @property
    def game_title(self) -> str:
        """Название игры"""
        return self._game_title
    
    @game_title.setter
    def game_title(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Название игры должно быть непустой строкой")
        self._game_title = value
    
    @property
    def max_players(self) -> int:
        """Максимальное количество игроков"""
        return self._max_players
    
    @max_players.setter
    def max_players(self, value: int):
        if not isinstance(value, int) or value < 1 or value > 4:
            raise ValueError("Количество игроков должно быть от 1 до 4")
        self._max_players = value
    
    @property
    def starting_resources(self) -> int:
        """Стартовые ресурсы"""
        return self._starting_resources
    
    @starting_resources.setter
    def starting_resources(self, value: int):
        if not isinstance(value, int) or value < 100:
            raise ValueError("Стартовые ресурсы должны быть не менее 100")
        self._starting_resources = value
    
    @property
    def map_size(self) -> tuple:
        """Размер карты (ширина, высота)"""
        return self._map_size
    
    @map_size.setter
    def map_size(self, value: tuple):
        if not isinstance(value, tuple) or len(value) != 2:
            raise ValueError("Размер карты должен быть кортежем из двух чисел")
        width, height = value
        if not (5 <= width <= 20 and 5 <= height <= 20):
            raise ValueError("Размер карты должен быть от 5x5 до 20x20")
        self._map_size = value
    
    @property
    def difficulty(self) -> str:
        """Сложность игры"""
        return self._difficulty
    
    @difficulty.setter
    def difficulty(self, value: str):
        valid_difficulties = ["easy", "normal", "hard", "expert"]
        if value not in valid_difficulties:
            raise ValueError(f"Сложность должна быть одной из: {valid_difficulties}")
        self._difficulty = value
    
    @property
    def game_version(self) -> str:
        """Версия игры"""
        return self._game_version
    
    @game_version.setter
    def game_version(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Версия игры должна быть строкой")
        self._game_version = value
    
    @property
    def auto_save(self) -> bool:
        """Автосохранение"""
        return self._auto_save
    
    @auto_save.setter
    def auto_save(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("Автосохранение должно быть булевым значением")
        self._auto_save = value
    

    
    # === Методы для работы с файлами ===
    
    def to_dict(self) -> Dict[str, Any]:
        """Преобразование объекта в словарь для JSON"""
        return {
            "game_title": self._game_title,
            "max_players": self._max_players,
            "starting_resources": self._starting_resources,
            "map_size": {
                "width": self._map_size[0],
                "height": self._map_size[1]
            },
            "difficulty": self._difficulty,
            "game_version": self._game_version,
            "auto_save": self._auto_save,
            
        }
    
    def save_to_file(self, filename: str = None) -> bool:
        """Сохранение конфигурации в JSON файл"""
        try:
            if filename is None:
                filename = self._config_file
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)
            
            print(f"✅ Конфигурация сохранена в файл: {filename}")
            return True
        except Exception as e:
            print(f"❌ Ошибка сохранения конфигурации: {e}")
            return False
    
    def load_from_file(self, filename: str = None) -> bool:
        """Загрузка конфигурации из JSON файла"""
        try:
            if filename is None:
                filename = self._config_file
            
            if not os.path.exists(filename):
                print(f"📝 Файл конфигурации не найден, используются значения по умолчанию")
                return False
            
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Загружаем данные с проверкой типов
            self._game_title = data.get("game_title", self._game_title)
            self._max_players = data.get("max_players", self._max_players)
            self._starting_resources = data.get("starting_resources", self._starting_resources)
            
            map_data = data.get("map_size", {})
            self._map_size = (
                map_data.get("width", self._map_size[0]),
                map_data.get("height", self._map_size[1])
            )
            
            self._difficulty = data.get("difficulty", self._difficulty)
            self._game_version = data.get("game_version", self._game_version)
            self._auto_save = data.get("auto_save", self._auto_save)
        
            
            print(f"✅ Конфигурация загружена из файла: {filename}")
            return True
        except Exception as e:
            print(f"❌ Ошибка загрузки конфигурации: {e}")
            return False
    
    def display_config(self):
        """Отображение текущей конфигурации"""
        print(f"\n⚙️  ТЕКУЩАЯ КОНФИГУРАЦИЯ ИГРЫ:")
        print(f"   🎮 Название: {self.game_title}")
        print(f"   👥 Макс. игроков: {self.max_players}")
        print(f"   💰 Стартовые ресурсы: {self.starting_resources}")
        print(f"   🗺️  Размер карты: {self.map_size[0]}x{self.map_size[1]}")
        print(f"   🎯 Сложность: {self.difficulty}")
        print(f"   🔄 Версия: {self.game_version}")
        print(f"   💾 Автосохранение: {'Вкл' if self.auto_save else 'Выкл'}")
       
    
    def update_config_interactive(self):
        """Интерактивное обновление конфигурации"""
        print(f"\n⚙️  ИЗМЕНЕНИЕ КОНФИГУРАЦИИ ИГРЫ")
        
        try:
            # Название игры
            new_title = input(f"Название игры [{self.game_title}]: ") or self.game_title
            self.game_title = new_title
            
            # Количество игроков
            new_players = input(f"Макс. игроков (1-4) [{self.max_players}]: ") or str(self.max_players)
            self.max_players = int(new_players)
            
            # Стартовые ресурсы
            new_resources = input(f"Стартовые ресурсы (≥100) [{self.starting_resources}]: ") or str(self.starting_resources)
            self.starting_resources = int(new_resources)
            
            # Размер карты
            new_width = input(f"Ширина карты (5-20) [{self.map_size[0]}]: ") or str(self.map_size[0])
            new_height = input(f"Высота карты (5-20) [{self.map_size[1]}]: ") or str(self.map_size[1])
            self.map_size = (int(new_width), int(new_height))
            
            # Сложность
            print("Доступные сложности: easy, normal, hard, expert")
            new_difficulty = input(f"Сложность [{self.difficulty}]: ") or self.difficulty
            self.difficulty = new_difficulty
            
            # Автосохранение
            auto_save_input = input(f"Автосохранение (y/n) [{'y' if self.auto_save else 'n'}]: ") 
            self.auto_save = auto_save_input.lower() == 'y' if auto_save_input else self.auto_save
            
        
            print("✅ Конфигурация обновлена!")
            
        except ValueError as e:
            print(f"❌ Ошибка ввода: {e}")
        except Exception as e:
            print(f"❌ Ошибка: {e}")


# Пример использования
if __name__ == "__main__":
    # Создаем объект конфигурации
    config = GameConfig()
    
    # Показываем текущую конфигурацию
    config.display_config()
    
    # Сохраняем в файл
    config.save_to_file()
    
    # Обновляем конфигурацию
    config.update_config_interactive()
    
    # Сохраняем обновленную конфигурацию
    config.save_to_file()
    
    # Создаем новый объект и загружаем из файла
    print("\n" + "="*50)
    print("Тестирование загрузки конфигурации...")
    new_config = GameConfig()
    new_config.display_config()