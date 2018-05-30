nums = [3,2,4]
target = 6


#def two_sum(nums, target)
#  twonums = []
#  nums.each do |num1|
#    num_pre = nums.select {|num2| num2 == target - num1}
#    twonums << nums.index(num_pre[0])
#  end
#  print [twonums.flatten[1], twonums.flatten[0]]
#end


def two_sum(nums, target)
    search = {}
    nums.each_with_index do |num,i|
      return [search[target-num], i] unless search[target-num].nil?
      search[num] = i
    end
end


two_sum(nums, target)
