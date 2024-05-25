import unittest
import dotenv

from .context import Authorization


class TestAuthorization(unittest.TestCase):
    # TODO
    def clear_test_env():
        pass

    def test_token_refresh_required_empty_expiry(self):
        env_file_path = "./tests/test.env"
        env_file = dotenv.dotenv_values(env_file_path)
        
        dotenv.set_key(env_file_path, "ACCESS_TOKEN", "TEST TOKEN")
        dotenv.set_key(env_file_path, "ACCESS_TOKEN_EXPIRATION", "")

        authorization = Authorization.Authorization(env_file, env_file_path)
        result = authorization.token_refresh_required(env_file["ACCESS_TOKEN_EXPIRATION"])
        self.assertEqual(result, True, "The result is False")

if __name__ == '__main__':
    unittest.main()