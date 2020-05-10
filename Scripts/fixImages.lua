
function Image(el)
	return pandoc.Image(
				el.title, 
				string.gsub(el.src, "^/", ""), 
				"asd"
				)
--  return pandoc.Image(s, src, tit, attr)
end