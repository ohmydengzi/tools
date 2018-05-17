#encoding:utf-8
"""
以下是实现去重的方法，并且实现了doctest，也就是以 >>> 这样的特殊格式写上函数调用和返回结果，实现相关用例的测试。
Come from @denglj
"""

def delete_reoccurring_chars(string):
  """
  return the string after deduplication
  >>> delete_reoccurring_chars('metasotaaa')
  'metasota'
  >>> delete_reoccurring_chars('metaaaasotaaa')
  'metasota'
  >>> delete_reoccurring_chars('metasota')
  'metasota'
  >>> delete_reoccurring_chars('')
  ''
  """
  return ''.join(v for i, v in enumerate(string) if string[i-1] != v)
"""
Equals to:
  return_string = ''
  for i, v in enumerate(string):
    if string[i-1] != v:
      return_string = return_string + v
  return return_string      
"""

if __name__ == "__main__":
  import doctest
  doctest.testmod()

