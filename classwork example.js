// JS — two pointers converging on a sorted array
function hasPairWithSum(nums, target) {
  let left = 0, right = nums.length - 1;
  while (left < right) {
    const sum = nums[left] + nums[right];
    if (sum === target) return true;
    if (sum < target) left++;
    else right--;
  }
  return false;
}


# Given a sorted array of numbers and a target value, I need to think of a way to find whether it has two distinct elements that sum up to the target. #

# does it return true or false #

# I believe in my thinking it will return true #