import os
import unittest

def run_all_tests():
    project_root = os.path.expanduser(r"C:\Users\krpri\OneDrive\Desktop\co pilot work\ai_soul_core")
    test_dir = os.path.join(project_root, "tests")

    print(f"Running all unittests from: {test_dir}")

    # Load and run all test cases
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=test_dir, pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED.")
    else:
        print(f"\n❌ TESTS FAILED: {len(result.failures)} failed, {len(result.errors)} errors.")

if __name__ == "__main__":
    run_all_tests()
