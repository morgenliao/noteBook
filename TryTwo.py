import tensorflow
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# OP_HELLO 的类型为 tensorflow.python.framework.ops.Tensor
OP_HELLO = tensorflow.constant('Hello, Tensor Flow!')
# SESSION 的类型为 tensorflow.python.client.session.Session
SESSION = tensorflow.Session()
# 输出结果为：
# b'Hello, Tensor Flow!'
print(SESSION.run(OP_HELLO))
# end of file
