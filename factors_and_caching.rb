#the factorize function computes the factors of each number in the given array and displays the output
def factorize(arr)
    arr.each do |num1|
        factorarray =[]
        print "Factors of #{num1}: "
        arr.each do |num2|
            if num1%num2 ==0 and num1!=num2
                factorarray.push(num2) unless factorarray.include?(num2)
            end
        end
        print "#{factorarray}\n"
    end
end

#the memoize function checks to see whether we have a cached value if we don't have the value, the value is placed in the cache and then the result is returned.
def memoize(fn)
    cache = {} 
    lambda {|*args|
        return cache[args] if cache.has_key?(args)
        cache[args] = fn.call(*args)}
end

#this function makes use of the of memoize (caching) function for duplicate values
memoize def caching_factorize(arr)
    arr.each do |num1|
        factorarray =[]
        print "Factors of #{num1}: "
        arr.each do |num2|
            if num1%num2 ==0 and num1!=num2
                factorarray.push(num2) unless factorarray.include?(num2)
            end
        end
        print "#{factorarray}\n"
    end
end


#test cases
puts "\nRegular factorization without the use of caching"
factorize([10, 5, 2, 20])
puts "\nFactorization with the use of caching"
caching_factorize([10, 5, 2, 20])

