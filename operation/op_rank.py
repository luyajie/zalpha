from operation.operation_base import OperationBase
import util

class OperationRank(OperationBase):
    def __init__(self, params, context):
        super().__init__(params, context)

    def initialize(self):
        pass

    def after_day(self, di, alpha):
        # Should return alpha as a list
        util.rank(alpha)
        return alpha