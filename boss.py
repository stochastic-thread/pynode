import json
import http


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

def wrap_content(tag_label, content,debug=True):
  tag_wrap = tag(tag_label="h1", both=True)
  if debug:
    print(tag_wrap)
  return tag_wrap[0]+content+tag_wrap[1]

def test_add_tag(tags_to_test=['html','head', 'title', 'body']):
  docs = []
  for item in tags_to_test:
    docs.append(item)

def main():
  wrap_content('h1', 'Arthur Maroufi Colle')
  
if __name__ == "__main__":
    main()


# def build_html_document(opts={meta=[]}):
#  add  
  
