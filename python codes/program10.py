clc;             
close all;       
clear all;       

b = input('Enter the numerator coefficients: ');
a = input('Enter the denominator coefficients: ');

zplane(b, a);    % Plot poles and zeros in the z-plane
