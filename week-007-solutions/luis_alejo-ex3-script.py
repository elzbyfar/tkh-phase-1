def script(*strings):
    
    open_file = open('output.html', 'w')
    open_file.write("<body>")
    
    for s in strings[1:]:
        open_file.write(s + ' ')
        
    open_file.write("</body>")
    open_file.close()
    
    return f"Successfully wrote {len(strings)} words onto output.html."

if __name__ == '__main__':
    import sys
    script(*sys.argv)