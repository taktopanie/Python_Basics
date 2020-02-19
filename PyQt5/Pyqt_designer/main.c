/* PROGRAM ��CZ�CY MIKROKONTROLER Z KOMPUTEREM ZA POMOC� UART
*/

#include<avr/io.h>
#include<avr/interrupt.h>
#include<util/delay.h>
#include<string.h>
#include<stdlib.h>
#include"UART_obsluga.h"
//#include"UART_obsluga.c"

//definicje zmiennych

volatile uint8_t stan;
uint8_t stan1;

char tmp_zdanie[20];
char zdanie[20];

float pomiar (int);


int main (void){

///////////////////////////////////////////////// CZYNNOSCI WSTEPNE////////////////////////////
// Pin PD5/PD6/PD7 jako wyjscie dla diod
DDRC|=(1<<PC5)|(1<<PC4)|(1<<PC3);
PORTC&=~(1<<PC5)&~(1<<PC4)&~(1<<PC3);

// Pin PB1 DLA PRZEKAZNIKA
DDRB|=(1<<PB1);
PORTB|=(1<<PB1);


//napiecie referencyjne 5v z mikrokontrolera
	ADMUX|=(1<<REFS0);
// wlaczenie ADC i ustawienie preskalera
	ADCSRA|=(1<<ADEN)|(1<<ADPS1)|(1<<ADPS2);

	DDRC|=(1<<PC0);
	PORTC&=~(1<<PC0);

char tmp_zmienna;
inicjacja_usart();

// URUCHOMIENIE PWM
DDRD|=(1<<PD5);
	//TCCR0A |=(1<<WGM01)|(1<<WGM00);//Tryb FAST PWM
//	TCCR0A |=(1<<COM0B1);//|(1<<COM0B0);//Clear OC0B on Compare Match, set OC0B at BOTTOM
	//TCCR0B |=(1<<CS00);//|(1<<CS02);//preskaler 1

//..TCCR0A |=(1<<WGM00);//Tryb fast PWM (clear OC0A on compare match)
//..TCCR0B |=(1<<WGM02);//Tryb fast PWM

//..TCCR0A |=(1<<COM0B1)|(1<<COM0B0);//Clear OC0B on Compare Match when up-counting. Set OC0B on Compare Match when down-counting.

//..TCCR0B |=(1<<CS01);//|(1<<CS02);//preskaler 8 czyli (8 000 000/8 = 1 000 000)
//..OCR0A=100;// maksymalny zabkres od 0 do OCR0A czyli (0-1000) 1kHz    zmiana stanu gdy osiegnie OCR0B


////////////////////////////////////////////////////////////////////////////////////////////////
WYSYLANIE_TEXTU("PROGRAM DZIALA\n\n");
while(1){

// pobranie zmiennej z bufora UART
tmp_zmienna = GET_BYTE();
static int i = 0;
int n;
	if(tmp_zmienna){

		if(tmp_zmienna =='+'){
			// przepisuje zdanie bez ostatniego znaku aby porownac je z haslem
			WYSYLANIE_TEXTU("\n");
			//WYSYLANIE_TEXTU(tmp_zdanie);
			//WYSYLANIE_TEXTU("\n");
			for(n=0;n<strlen(tmp_zdanie);n++){
				zdanie[n]=tmp_zdanie[n];
			}
			i=0;
			// FUNKCJE WYKONUJACE ODPOWIEDNIE CZYNNOSCI W ZALEZNOSCI OD SZYFRU
			if(strcmp(zdanie,"#01*00")==0){
				PORTC&=~(1<<PC5)&~(1<<PC4)&~(1<<PC3);
			// RESET DIOD
			}else if(strcmp(zdanie,"#01*11")==0){
				PORTC|=(1<<PC5);
				//WYSYLANIE_TEXTU("\nzapalenie diody nr 1 \n");
			}else if(strcmp(zdanie,"#01*10")==0){
				PORTC&=~(1<<PC5);
				//WYSYLANIE_TEXTU("\nzgaszenie diody nr 1 \n");
			}else if(strcmp(zdanie,"#01*21")==0){
				PORTC|=(1<<PC4);
				//WYSYLANIE_TEXTU("\nzapalenie diody nr 2 \n");
			}else if(strcmp(zdanie,"#01*20")==0){
				PORTC&=~(1<<PC4);
				//WYSYLANIE_TEXTU("\nzgaszenie diody nr 2 \n");
			}else if(strcmp(zdanie,"#01*31")==0){
				PORTC|=(1<<PC3);
				//WYSYLANIE_TEXTU("\nzapalenie diody nr 3 \n");
			}else if(strcmp(zdanie,"#01*30")==0){
				PORTC&=~(1<<PC3);
				//WYSYLANIE_TEXTU("\nzgaszenie diody nr 3 \n");
			}else if(strcmp(zdanie,"#02*11")==0){
				double wartosc_pomiaru = pomiar(0);
				wartosc_pomiaru=wartosc_pomiaru*5/1024;
				char zmienna_do_wysw[2];
				dtostrf(wartosc_pomiaru,2,2,zmienna_do_wysw);
				WYSYLANIE_TEXTU("/");
				WYSYLANIE_TEXTU(zmienna_do_wysw);
				WYSYLANIE_TEXTU("\n");
				// FUNKCJA OD PWM
			}else if(strcmp(zdanie,"#03*11")==0){
				PORTB^=(1<<PB1);
				OCR0B=100;
				//if(OCR0B>=100){
				//	OCR0B=0;
				//}
				// FUNKCJA DO TESTOWANIA KOMUNIKACJI
			}else if(strcmp(zdanie,"#04*11")==0){
				WYSYLANIE_TEXTU("TESTOWY TEKST");
				PORTD^=(1<<PD5);
				// GDY ZADNA Z WYMIENIONYCH KOMEND NIE PASUJE
			}else WYSYLANIE_TEXTU("Nieznana komenda.");



			// WYZEROWANIE ZMIENNYCH ZDANIE ABY ZAPISAC JA KOLEJNYMI DANYMI
				for(n = 0; n<20; n++)
				{
					tmp_zdanie[n]=0;
					zdanie[n]=0;
				}
			// DODAWANIE ZMIENNEJ DO ZDANIA
			}else{
			tmp_zdanie[i]=tmp_zmienna;
			i++;
			}
		}
	}
}


float pomiar (int ch){
			// zapis ktorego kanalu chce uzyc
			ADMUX = (ADMUX & 0xF8) | ch;
			// start pomiaru
			ADCSRA |=(1<<ADSC);
			//dopoki nie zwroci 0
			while(ADCSRA & (1<<ADSC));
			return ADCW;
	}
