
s = "egg"
t = "add"

#s = "foo", t = "bar"

#s = "paper", t = "title"

def is_isomorphic(s, t)
  s = s.split(//)
  s_dup = s.detect {|dup| s.count(dup) > 1}
  s_dup_inx = s.each_index.select{|ind| s[ind] == s_dup}

  t = t.split(//)
  t_dup = t.detect {|dup| t.count(dup) > 1}
  t_dup_inx = t.each_index.select{|ind| t[ind] == t_dup}

  return s_dup_inx == t_dup_inx
end

is_isomorphic(s,t)
# sure return true or false

