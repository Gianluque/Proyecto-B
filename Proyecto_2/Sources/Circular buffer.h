#define BUFF_SIZE (9U)


// Estructura tipo buffer, donde se almacenara la data
typedef struct buffer {
	
    char buff[BUFF_SIZE];
    unsigned writeIndex;  
}buffer;

// Proceso de escritura del buffer
void write(struct buffer *buffer, char value) {
    buffer->buff[(++buffer->writeIndex) % BUFF_SIZE] = value;
}

// Proceso de lectura del buffer, se toma el valor mas reciente almacenado
char readn(struct buffer *buffer, unsigned Xn){
    return buffer->buff[(buffer->writeIndex - Xn) % BUFF_SIZE];
}

// Filtro de la data
int fir(buffer *buffercito, char coef[], char tap ){

    int output=0;
    char *ptrco = coef;
    char i;

    for (i=0;i<=tap && *ptrco != 0;i++){
         // Se toma el valor mas reciente  del buffer y se multiplica por el primer valor del coeficiente   
		output+= (readn(buffercito,i)) * *ptrco++;
    }
 return output;

}
