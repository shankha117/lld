import json


class SpeechMatics(object):

    def __init__(self, **kwargs):
        self._stt_name = "speechmatics"
        self._sm_url = kwargs['url']
        self._sm_params = "newparams"
        self._diarization = kwargs['diarization']
        self._sm_param = "sm_param"

    def send_audio(self, data):
        data = "somedata sent"
        idd = "transcribing"
        return idd

    def get_data(self, sm_id):
        get_data_sm = "transcribing with SM"
        return get_data_sm

    def transcribe_with_sm(self, data):
        idd = self.send_audio(data)
        data = self.get_data(idd)
        return data

    def __str__(self):
        return json.dumps(self.__dict__)


class Microsoft(object):

    def __init__(self, **kwargs):
        self._stt_name = "microsoft"
        self._mics_url = kwargs['url']
        self._sm_params = "newparams_ms"
        self._output = kwargs['output_type']
        self._mics_param = "mics_param"

    def send_audio(self, data):
        data = "somedata sent"
        idd = "transcribing"
        return idd

    def get_data(self, sm_id):
        get_data_sm = "transcribing with MicS"
        return get_data_sm

    def transcribe_with_ms(self, data):
        idd = self.send_audio(data)
        data = self.get_data(idd)
        return data

    def __str__(self):
        return json.dumps(self.__dict__)


class Adapter(object):

    def __init__(self, object, **adapter_method):
        self._object = object

        self.__dict__.update(adapter_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


def main():
    objects = []
    sppechmatics_engine = SpeechMatics(url="someurl", diarization=True)
    microsoft = Microsoft(url="someurl", output_type="json")

    objects.append(Adapter(sppechmatics_engine, transcribe=sppechmatics_engine.transcribe_with_sm))
    objects.append(Adapter(microsoft, transcribe=microsoft.transcribe_with_ms))

    for obj in objects:
        print(obj._object)
        print(obj.transcribe("here is some data"))


if __name__ == "__main__":
    main()
