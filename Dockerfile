FROM faucet/python3:10.0.0

COPY . /area6/python/dev/markdownpy/

WORKDIR /area6/python/dev/markdownpy/

#RUN rm -r venv

RUN python -m venv venv
RUN pip install markdown
RUN pip install flask

EXPOSE 8080

CMD /area6/python/dev/markdownpy/startup.sh

# docker build -t lmldocker/markdownpy:1.0 .
# docker run -it --rm -p 8080:8080 lmldocker/markdownpy:1.0
