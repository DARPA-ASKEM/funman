"""
This module defines enocoders for already encoded models.  (Technically, a
pass-through that helps make the encoder abstraction uniform.)
"""
from funman.model import Model
from funman.model.encoded import EncodedModel
from funman.translate import Encoder, Encoding, EncodingOptions
from funman.translate.translate import LayeredEncoding


class EncodedEncoder(Encoder):
    """
    An EncodedEncoder assumes that a model has already been encoded as an
    EncodedModel, and acts as a noop to maintain consistency with other
    encoders.
    """

    def encode_model(self, model: Model):
        """
        Encode the model by returning the already encoded formula.

        Parameters
        ----------
        model : Model
            Encoded model

        Returns
        -------
        FNode
            SMTLib formula encoding the model
        """
        if isinstance(model, EncodedModel):
            encoding = LayeredEncoding(
                _layers=[
                    (model._formula, list(model._formula.get_free_variables()))
                ],
            )
            return encoding
        else:
            raise Exception(
                f"An EncodedEncoder cannot encode models of type: {type(model)}"
            )

    def _encode_timed_model_elements(self, scenario: "AnalysisScenario"):
        pass

    def encode_model_timed(
        self, scenario: "AnalysisScenario", num_steps: int, step_size: int
    ) -> Encoding:
        return self.encode_model(scenario.model)
