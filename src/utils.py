import json

class NullToNoneDecoder(json.JSONDecoder):
    def decode(self, s):
        result = super().decode(s)
        return self._process(result)

    def _process(self, obj):
        if isinstance(obj, dict):
            return {k: self._process(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._process(v) for v in obj]
        elif obj is None:
            return None
        else:
            return obj
