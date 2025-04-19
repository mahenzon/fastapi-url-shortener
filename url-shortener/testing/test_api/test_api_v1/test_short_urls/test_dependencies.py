from api.api_v1.short_urls.dependencies import UNSAFE_METHODS


def test_unsafe_methods_doesnt_contain_safe_methods() -> None:
    safe_methods = {
        "GET",
        "HEAD",
        "OPTIONS",
    }
    assert not UNSAFE_METHODS & safe_methods
