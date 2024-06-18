% Calculate weight of wire based on transmission voltage 
clc 
clear 

p = 1500; % watts 
res_cu = 1.7e-8; %ohms 
res_al = 2.8e-8; 
rho_cu = 8940; %kg/m^3 
rho_al = 2700; 
rho_ins = 860; %kg/m^3 for ethylene polypropylene rubber 
l = 0:100:50000; % length, meters 

lossVec = [0.02];% total wire losses (percentage of the power) 

for i = 1:length(lossVec) 
loss = lossVec(i); 
V = 400:100:3000; %line-line voltages, rms 
%V = V*(sqrt(3)); 
% AC 
I = p./(sqrt(3)*V); % RMS current in each line 
Vdrop = loss*V; %voltage drop across the wire for each phase 

thick_ins_AC = .0254*(8.1e-6*(V*sqrt(2)) + .057); %thickness in meters 
thick_ins_DC = .0254*(8.1e-6*V + .057); %thickness in meters 

A_al = []; %cross sectional area 
for k = 1:length(l) 
    A_al(k) = res_al * l(k) * I ./ Vdrop;
    if A_al(k) < 1.33e-6 
        A_al(k) = 1.33e-6; 
    end 
end 
m_al = A_al*l*rho_al; % total mass for one wire(one phase) 
m_ins_al = (pi*((sqrt(A_al/pi)+thick_ins_AC).^2)-A_al)*l*rho_ins; 
m_al_tot = 3*(m_al + m_ins_al); % model using 3x mass_al +3x mass_ins, 

A_cu = res_cu * l * I ./ Vdrop; 
m_cu = 1*A_cu*l*rho_cu; 
m_ins_cu = (pi*((sqrt(A_cu/pi)+thick_ins_AC).^2)-A_cu)*l*rho_ins; 
m_cu_tot = 3*(m_cu + m_ins_cu); 

% DC 
Idc = p./V; %DC voltage 

Adc_cu = res_cu * (2*l) * Idc./ Vdrop; %cross sectional area, for one wires 
mdc_cu = Adc_cu*l*rho_cu; % total mass for one wires 
Rdc_cu = res_cu*l./Adc_cu; % resistance per wire 
mdc_ins_cu = (pi*((sqrt(Adc_cu/pi)+thick_ins_DC).^2)-Adc_cu)*l*rho_ins; 
mdc_cu_tot = 2*(mdc_cu + mdc_ins_cu); 

Adc_al = res_al * (2*l) * Idc./ Vdrop; %cross sectional area, for two wires 
for n = 1:length(V) 
if Adc_al(n) < 1.33e-6 %assumes that limit for aluminum is AWG 6 
Adc_al(n) = 1.33e-6; 
end 
end 
mdc_al = 1*Adc_al*l*rho_al; % total mass for one wire 
Rdc_al = res_al*l./Adc_al; 
mdc_ins_al = (pi*((sqrt(Adc_al/pi)+thick_ins_DC).^2)-Adc_al)*l*rho_ins; 
mdc_al_tot = 2*(mdc_al + mdc_ins_al); 

%figure 
%plot(V,m_al,V,m_ins_al,V,m_al_tot) 
%legend(‘Aluminum’,’Insulation’,’Total’) 
%title(‘Weight Composition for AC Aluminum Cables’) 
%xlabel(‘Line-line Voltage [V]’) 
%ylabel(‘Conductor weight [kg]’) 
%grid on 

%figure 
%plot(V,m_cu,V,m_ins_cu,V,m_cu_tot) 
%legend(‘Copper’,’Insulation’,’Total’) 
%title(‘Weight Composition for AC Copper Cables’) 
%xlabel(‘Line-line Voltage [V]’) 
%ylabel(‘Conductor weight [kg]’) 
%grid on 

%figure 
%plot(V,mdc_cu,V,mdc_ins_cu,V,mdc_cu_tot) 
%legend(‘Copper’,’Insulation’,’Total’) 
%title(‘Weight Composition for DC Copper Cables’) 
%xlabel(‘Line-line Voltage [V]’) 
%ylabel(‘Conductor weight [kg]’) 
%grid on 

%figure 
%plot(V,mdc_al,V,mdc_ins_al,V,mdc_al_tot) 
%legend(‘Aluminum’,’Insulation’,’Total’) 
%title(‘Weight Composition for DC Aluminum Cables’) 
%xlabel(‘Line-line Voltage [V]’) 
%ylabel(‘Conductor weight [kg]’) 
%grid on 

figure 
%semilogy(V,m_cu_tot,V,m_al_tot,V,mdc_cu_tot,V,mdc_al_tot) 
plot(V,m_cu_tot,V,m_al_tot,V,mdc_cu_tot,V,mdc_al_tot) 
legend('AC Cu','AC Al','DC Cu','DC Al') 
title('Weight Comparison with 2% losses') 
xlabel('Line-line Voltage [V]') 
ylabel('Conductor weight [kg]') 
grid on 
end 