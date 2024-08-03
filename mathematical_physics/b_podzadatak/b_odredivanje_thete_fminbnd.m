g = 8.91;
v0 = 10;

%trazenje maksimuma pocetne funkcije svodim na trazenje minimuma
%noj negativne funkcije
F = @(theta) -(v0^2 * cos(theta) * (1 - 1/(sin(theta) + 1))) / g;
opts = optimset('TolX', 1e-8);

theta_min = 0;
theta_max = pi/2;
[theta_max, F_max]= fminbnd(F, theta_min, theta_max, opts);
F_max = -F_max;

disp('Theta koje maksimizira funkciju: ');
disp(theta_max)


