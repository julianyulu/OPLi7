FILES :=				\
	constant.py			\
	optPumping.py			\
	TransitionStrength.py		\
	plot.py				\
	functions.py			\
	singleRun.py			\
	laserDetuneScan.py		\
	laserIntensityScan.py		\
	singleRun.in			\
	laserIntensityScan.in		\
	laserDetuneScan.in		\

test:
	python3 examples/example_single_run.py
check:
	@not_found=0;                             \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
	echo "success";

clean:
	rm -f *.pyc
	rm -f *~
	rm -rf __pycache__

