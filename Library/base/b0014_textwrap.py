import textwrap

long_text = "In the journey of achieving your dreams, \
remember that success is not final, failure is not fatal: \
it is the courage to continue that counts. \
Every setback is a chance to learn and grow, \
and every victory is just a step towards your next challenge. \
Stay resilient and keep moving forward."

wrapped_text = textwrap.fill(long_text, width=60)
print(wrapped_text)

# output:
# In the journey of achieving your dreams, remember that
# success is not final, failure is not fatal: it is the
# courage to continue that counts. Every setback is a chance
# to learn and grow, and every victory is just a step towards
# your next challenge. Stay resilient and keep moving forward.

wrapped_list = textwrap.wrap(long_text, width=60)
for line in wrapped_list:
    print(line)

# 결과:
# In the journey of achieving your dreams, remember that
# success is not final, failure is not fatal: it is the
# courage to continue that counts. Every setback is a chance
# to learn and grow, and every victory is just a step towards
# your next challenge. Stay resilient and keep moving forward.

wrapped_text = textwrap.fill(long_text, width=60)

# Indentation
indented_text = textwrap.indent(wrapped_text, prefix='    ')
print(indented_text)

# output :
#     In the journey of achieving your dreams, remember that
#     success is not final, failure is not fatal: it is the
#     courage to continue that counts. Every setback is a chance
#     to learn and grow, and every victory is just a step towards
#     your next challenge. Stay resilient and keep moving forward.


# Indentation delete
dedented_text = textwrap.dedent(indented_text)
print(dedented_text)

# output :
# In the journey of achieving your dreams, remember that
# success is not final, failure is not fatal: it is the
# courage to continue that counts. Every setback is a chance
# to learn and grow, and every victory is just a step towards
# your next challenge. Stay resilient and keep moving forward.

# Reduce
shortened_text = textwrap.shorten(long_text, width=50, placeholder="...")
print(shortened_text)

# output :
# This is a very long piece of text that needs to...

import textwrap

# TextWrapper initial
wrapper = textwrap.TextWrapper(width=60, initial_indent='* ', subsequent_indent='  ')
wrapped_text = wrapper.fill(long_text)
print(wrapped_text)

# output:
# * In the journey of achieving your dreams, remember that
#   success is not final, failure is not fatal: it is the
#   courage to continue that counts. Every setback is a chance
#   to learn and grow, and every victory is just a step
#   towards your next challenge. Stay resilient and keep
#   moving forward.