#!/usr/bin/env ruby

#scan for sync word
#syncword = /0010110111010100/
syncword = [0x2d, 0xd4]

#scan for data
#  {0xff, 0x00, 0xff, 0x00, 0xff, 0x00, 0xff};
#data = /11111111000000001111111100000000111111110000000011111111/
#  {0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77};
#data = /00010001001000100011001101000100010101010110011001110111/
# {0x5a, 0x61, 0x6b, 0x48, 0x65, 0x6c, 0x6c};
#data = /01011010011000010110101101001000011001010110110001101100/
data = "ZakHell"

#scan for preambule
preambule = [0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa]
#preambule = [0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55]

def split_word(s)
  0.upto(s.length - 1).flat_map do |start| 
    2.upto(s.length - start).map do |length| 
      s[start, length]
    end
  end.uniq.sort_by {|x| x.length}.reverse
end

def find_occurence(d, data, dname)
    if data.is_a?(String)
	bdata = data.unpack("B*").map {|x| x.to_s}.join
    elsif data.is_a?(Array)
        bdata = data.map {|n| "%08b" % n}.join
    else
        bdata = data
    end
    
    di  = d.to_enum(:scan,bdata).map {Regexp.last_match.begin(0)}
    puts
    puts di.length.to_s + " Occurences of " + dname + "(pattern:" + data.to_s + ")" +" at indexes: "
    print di
    puts
end

def find_alloccurence(d, data, dname)
    print "#############################################"
    split_word(data).each_with_index {|val, index| find_occurence(d, val, dname + "#{index}")}
end

def savepacket(dataset, start, endi, filename)                                                                                                                        
  dd = [dataset[start..endi]].pack('B*')                                                                                                                              
  f2 = File.open(filename, 'wb')
  f2.write(dd)
  f2.close()
end  

fileIN  = ARGV[0]
fileOUT = ARGV[1]

if fileIN == nil 
   abort("Please provide a record file!")
end

if fileOUT == nil 
   abort("Please provide a record file!")
end

puts "Using file: " + fileIN

f = File.open(fileIN, 'rb')
dat = f.read();
d = dat.unpack("C*").map {|x| x.to_s}.join;

if 1 == 1
    find_occurence(d, preambule, "preambule")
    find_occurence(d, syncword, "syncword")
    find_occurence(d, data, "data")
else
    find_alloccurence(d, syncword, "syncword")
    find_alloccurence(d, preambule, "preambule")
    find_alloccurence(d, data, "data")
end

puts "Generating decoded file: " + fileOUT

dd = [d].pack('B*');
f2 = File.open(fileOUT, 'wb')
f2.write(dd)
f2.close()

f.close()
