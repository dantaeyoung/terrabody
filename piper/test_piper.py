import subprocess

phrase = "This is a test of piper."

print("TEST: You should hear 'this is a test of piper'.")

# Define the first part of the pipe
p1 = subprocess.Popen(['echo', phrase], stdout=subprocess.PIPE)

# Define the second part of the pipe
p2 = subprocess.Popen("./piper/piper --model piper/voices/en_GB-alan-medium.onnx --output-raw".split(" "), stdin=p1.stdout, stdout=subprocess.PIPE)

p3 = subprocess.Popen("aplay -r 22050 -f S16_LE -t raw -".split(" "), stdin=p2.stdout, stdout=subprocess.PIPE)


# Close the first process's output to allow p1 to receive a SIGPIPE if p2 exits
p1.stdout.close()
p2.stdout.close()

# Get the output
output = p3.communicate()[0]
print(output.decode())

