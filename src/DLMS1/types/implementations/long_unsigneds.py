from COSEMpdu.data import LongUnsigned


class ClassId(LongUnsigned):
    """ Class ID type """


class ServerSAP(LongUnsigned):

    def validate(self) -> None:  # TODO: make report
        if self.value > 0x3FFF:
            raise ValueError(F'The range for the server_SAP is 0x000…0x3FFF, but got {self.contents.hex()}')
