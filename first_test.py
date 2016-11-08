#!/usr/bin/env python
#coding=utf-8
import tensorflow as tf

#2
state = tf.Variable(0, name="counter")

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state,  new_value)

init_op = tf.initialize_all_variables()

#3
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.mul(input1, input2)

input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.mul(input1,intermed)



with tf.Session() as sess:
  print sess.run([output], feed_dict={input1:[7.], input2:[2.]})

  # for _ in range(3):
  #     sess.run(update)
  #     print sess.run(state)
