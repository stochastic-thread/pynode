import json
import http

def document_template(document_config={'title':'titre'}, content='Content'):
  return(wrap_content('html',
      wrap_content('head', wrap_content('title', document_config['title']))
      +wrap_content('body', wrap_content('div',''))))

def tag(tag_label, both=True, opening=None, closing=None):
  ret = None
  both = False
  if closing==None and opening==None:
    both=True
  if closing==True and opening==True:
    print("API will return both start and end tags.")
    print("     index 0 is start, index 1 is end.")
    both = True
  if closing==False and opening==False:
    both=True

  start_tag = '<'+tag_label+'>'
  end_tag = '</'+tag_label+'>'
  if both:
    return [start_tag, end_tag]
  else:
     if opening:
      ret = start_tag
     if closing:
       ret = end_tag
  return ret

def wrap_content(tag_label, content,debug=False):
  tag_wrap = tag(tag_label, both=True)
  labeled_tag_w_content = tag_wrap[0]+content+tag_wrap[1]
  if debug:
    print(labeled_tag_w_content)
  return labeled_tag_w_content

def test_add_tag(tags_to_test=['html','head', 'title', 'body']):
  docs = []
  for item in tags_to_test:
    docs.append(item)

def main():
  print(document_template(content=wrap_content('h1', 'Arty Farty')))
  print('\n')
  wrap_content('h1', 'Arthur Maroufi Colle', debug=True)

if __name__ == "__main__":
    main()
