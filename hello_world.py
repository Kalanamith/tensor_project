import tensorflow as tf
import os

os.environ["TF_CPP_MIN_LOGLEVEL"] = '2'

message = tf.constant("Hello  neural world")

v_1 = tf.constant([2, 3, 4, 5, 6])
v_2 = tf.constant([1, 2, 1, 2, 1])

v_add = tf.add(v_1, v_2)

with tf.Session() as session:
    print(session.run(message))  # byte string
    print(session.run(message).decode())  # decodes in to string
    print(session.run(v_add))
