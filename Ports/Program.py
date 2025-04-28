import sys
import importlib

class Program:

    @staticmethod
    def main(args):
        if not args:
            print("Error: Test name is required.")
            assert True

        test_name = args[0]  # Наприклад, NetworkCardSpeed01
        class_name = f"Ports.{test_name}"

        Program.execute(class_name)

    @staticmethod
    def execute(class_name):
        try:
            # Імпортуємо модуль і клас
            module_name, class_name_only = class_name.rsplit('.', 1)
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name_only)

            # Ініціалізуємо екземпляр
            instance = cls()

            # Отримуємо атрибути класу
            field_name = getattr(cls, "NAME", "Unknown")
            field_description = getattr(cls, "DESCRIPTION", "No Description")

            print(f"Start of test execution: {field_name}")
            print(f"Description: {field_description}\n")

            # Викликаємо методи Prepare, Run, Clean
            prepare = getattr(instance, "Prepare", None)
            run = getattr(instance, "Run", None)
            clean = getattr(instance, "Clean", None)

            if callable(prepare) and callable(run) and callable(clean):
                print("Executing Prepare...")
                prepare()
                print("Executing Run...")
                run()
                print("Executing Clean...")
                clean()
                print("\nTest completed successfully!")
            else:
                print("Error: Prepare, Run, or Clean method not found or not callable.")

        except ModuleNotFoundError:
            print(f"Error: Test module '{class_name}' not found. Make sure the module exists.")
        except AttributeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    Program.main(sys.argv[1:])
