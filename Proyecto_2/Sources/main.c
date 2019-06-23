/* ###################################################################
**     Filename    : main.c
**     Project     : Proyecto_2
**     Processor   : MC9S08QE128CLK
**     Version     : Driver 01.12
**     Compiler    : CodeWarrior HCS08 C Compiler
**     Date/Time   : 2019-06-19, 09:21, # CodeGen: 0
**     Abstract    :
**         Main module.
**         This module contains user's application code.
**     Settings    :
**     Contents    :
**         No public methods
**
** ###################################################################*/
/*!
** @file main.c
** @version 01.12
** @brief
**         Main module.
**         This module contains user's application code.
*/         
/*!
**  @addtogroup main_module main module documentation
**  @{
*/         
/* MODULE main */


/* Including needed modules to compile this module/procedure */
#include "Cpu.h"
#include "Events.h"
#include "AD1.h"
#include "AS1.h"
#include "Bit1.h"
#include "TI1.h"
#include "Led1.h"
#include "Bit2.h"
#include "Filtro.h"
#include "Filtrox.h"
#include "KB1.h"
#include "Muestreo.h"
/* Include shared modules, which are used for whole project */
#include "PE_Types.h"
#include "PE_Error.h"
#include "PE_Const.h"
#include "IO_Map.h"
#include "Circular buffer.h"
/* User includes (#include below this line is not maintained by Processor Expert) */
char flag =1;
char flagfir=1;


// Proceso de entramado de la data
void Entramado(unsigned int mask []){
	
	
		mask[2]=0;
		mask[2] = ((mask[0]>>4 & 0b0000100000000000) | mask[0]<<3) & 0b0000110000000000;
		mask[2] = ((mask[2] | mask[1]>>6) & 0b0000111000000000) | mask[1]<<1 & 0b0000111100000000;  
		
		mask[0] = (mask[0] & 0b0111111111111111) | 0b0000000010000000;
		mask[1] = mask[1] | 0b1000000010000000;
		mask[2] = mask[2] | 0b1000000000000000;
		
		
}

// Envio de bloque de 5 bytes.
void SendData(int out[]){
	char error;
	char ptr;
	do{
		// Se envia un bloque de 5 bytes se pierde un byte no usado ya que es un arreglo de enteros.
		error = AS1_SendBlock(out,5,&ptr);
		

	
	}while(error!=ERR_OK);
}



// Adquisicion de canales digitales
void Digitchan (int data []){
	
	if (Bit1_GetVal()==0) { data[2] = data[2] | 0b0100000000000000; }
	
	if (Bit2_GetVal()==0) { data[2] = data[2] | 0b0010000000000000; }
	
}




void main(void)
{
// Se declararon dos estructuras del tipo buffer ya que se necesitan almacenar dos canales analogicos
	buffer buffercito;
	buffer buffercito2;
	char coef [] = {1,0,-11,0,74,127,74,-11,0,1};  // Coeficientes del filtro
	char input [2];	// Entrada de la data
	int output[3];  // Salida de la data despues de ser filtrada
	char i=0; 		// Contador el cual lleva registro de cuantas multiplicaciones se han de realizar en el filtrado
	tap = 8; 		// orden del filtro
	// Localizacion inicial donde se almacena la data de los canales analogicos
	buffercito.writeIndex=0; 
	buffercito2.writeIndex=0;
	

  /*** Processor Expert internal initialization. DON'T REMOVE THIS CODE!!! ***/
  PE_low_level_init();
  /*** End of Processor Expert internal initialization.                    ***/

  for(;;){
	 
	 if (flag){ 
		 Muestreo_NegVal();
		 flag = 0;
		 AD1_Measure(TRUE);
		 AD1_GetValue(input);
		 
		 if(flagfir){
			 // Proceso de escritura de la data obtenida
		 	 write(&buffercito,input[0]);
		 	 write(&buffercito2,input[1]);
		 	 // filtrado de la data almacenandose en una variable tipo entero
		 	 output[0] = fir (&buffercito,coef,i);
		 	 output[1] = fir(&buffercito2,coef,i);
		 }else 
		 {	// caso alternativo si no se desea filtrar la data
		 	 output[0] = input[0];
		 	 output[1] = input[1];
		 }
		 
		 Entramado(output);
		 Digitchan(output);
		 SendData(output);
		 i++;
	  if(i == tap) i=0;} // Reinicio del contador para comenzar un nuevo filtrado de data
	 

	 
 }


  /*** Don't write any code pass this line, or it will be deleted during code generation. ***/
  /*** RTOS startup code. Macro PEX_RTOS_START is defined by the RTOS component. DON'T MODIFY THIS CODE!!! ***/
  #ifdef PEX_RTOS_START
    PEX_RTOS_START();                  /* Startup of the selected RTOS. Macro is defined by the RTOS component. */
  #endif
  /*** End of RTOS startup code.  ***/
  /*** Processor Expert end of main routine. DON'T MODIFY THIS CODE!!! ***/
  for(;;){}
  /*** Processor Expert end of main routine. DON'T WRITE CODE BELOW!!! ***/
} /*** End of main routine. DO NOT MODIFY THIS TEXT!!! ***/

/* END main */
/*!
** @}
*/
/*
** ###################################################################
**
**     This file was created by Processor Expert 10.3 [05.09]
**     for the Freescale HCS08 series of microcontrollers.
**
** ###################################################################
*/
