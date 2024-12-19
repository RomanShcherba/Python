import sys
import importlib

class Program:

    @staticmethod
    def main(args):
        if not args:
            print("Error: Test name is required.")
            return

        test_name = args[0]
        class_name = f"Ports.{test_name}"

        Program.execute(class_name)

    @staticmethod
    def execute(class_name):
        try:
            module_name, class_name_only = class_name.rsplit('.', 1)
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name_only)
            instance = cls()

            field_name = getattr(cls, "NAME", "Unknown")
            field_description = getattr(cls, "DESCRIPTION", "No Description")

            print(f"Start of test execution: {field_name}\nDescription: {field_description}\n")

            prepare = getattr(instance, "Prepare", None)
            run = getattr(instance, "Run", None)
            clean = getattr(instance, "Clean", None)

            if callable(prepare) and callable(run) and callable(clean):
                prepare()
                run()
                clean()
            else:
                print("Error: Prepare, Run, or Clean method not found.")

        except ModuleNotFoundError:
            print(f"Error: Test module '{class_name}' not found.")
        except AttributeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")