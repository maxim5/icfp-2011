SOLUTION=strategy_kill_all.py

dist:
	rm -rf .dist
	rm -rf solution.tar.gz
	mkdir .dist
	mkdir .dist/src
	touch .dist/install
	chmod a+x .dist/install
	cp $(SOLUTION) .dist/run
	cp lib.py .dist/
	cd .dist && tar pczvf ../solution.tar.gz *
#	tar -pczvf solution.tar.gz .dist/*

