%Codigo de graficado
while get(handles.On_Off,'Value')==1
    %busqueda de inicio y adquisicion de bytes
    aux=fread(puerto,[1,buffersize],'uint8'); 
        %flush del puerto
    flush=flush+1;
    if flush>2
    flushinput(puerto)
    flush=0;
    end
    i=1;
    while aux(i)>127
        i=i+1;
    end  
    dac=3/(2^16);

    bin=dec2bin(aux);    
    while i<(buffersize-4)
       chauxAlog1= strcat(bin(i+4,5),bin(i,2:8),bin(i+4,6),bin(i+1,2:8));
       chauxdig1= bin(i+4,3); 
       chauxAlog2= strcat(bin(i+4,7),bin(i+2,3:8),bin(i+4,8),bin(i+3,3:8)); 
       chauxdig2= bin(i+4,4);
       
               %shifteo y actualizacion de canales
        digit_1 = circshift(digit_1,1);
        digit_2 = circshift(digit_2,1);
        digit_1(1)=bin2dec(chauxdig1)*Amplitud_ch1*dac;
        digit_2(1)=bin2dec(chauxdig2)*Amplitud_ch2*dac;    
        ch1_plot = circshift(ch1_plot,1);
        ch2_plot = circshift(ch2_plot,1);        
        ch1_plot(1)=bin2dec(chauxAlog1)*Amplitud_ch1*dac;
        ch2_plot(1)=bin2dec(chauxAlog2)*Amplitud_ch2*dac;
        
        %Canales setm o plot
        
        if get(handles.plot_stem,'Value')==1
         %grafico de canales continuo
        cla;
        
        if get(handles.Alog_1,'Value')==1
        plot(time,ch1_plot,'b');
        end
        hold on;
        grid on;
        axis([0 5 0 5])
        if get(handles.Alog_2,'Value')==1
        plot(time,ch2_plot,'r');
        end
        if get(handles.Digi_1,'Value')==1
        plot(time,digit_1,'g');
        end
        if get(handles.Digi_2,'Value')==1
        plot(time,digit_2,'m');
        end
        drawnow;
        i=i+4;
        elseif get(handles.plot_stem,'Value')==2
        cla;    
        if get(handles.Alog_1,'Value')==1
        plot(time,ch1_plot,'b.');
        end
        hold on;        
        
        if get(handles.Alog_2,'Value')==1
        plot(time,ch2_plot,'r.');
        end
        if get(handles.Digi_1,'Value')==1
        plot(time,digit_1,'g.');
        end
        
        if get(handles.Digi_2,'Value')==1
        plot(time,digit_2,'m.');
        end
        drawnow;    
        end
        i=i+5;
    end

    %cla 
end

end
