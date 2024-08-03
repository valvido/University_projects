% za dani theta kreiram event koji zaustavlja integraciju kada
%funkcija dosegne y_B koordinatu po y osi
%trazim theta takav da je razlika x_B i koordinate minimalna

xB = 11.8475917655;
yB = 6.9851731350;
g = 9.81;
v0 = 20;
alpha = 0.2;
theta_min=0;
theta_mac = pi/2;




    x1 = 0;
    y2 = 0;
    v1 = v0 * cos(theta(i));
    v2 = v0 * sin(theta(i));
    uvjeti = [x1 x2 v1 v2];
    interval= [0,5]


   function x = solution(theta, F, v0, yB)
    F = @(t, y) [y(3); y(4); -alpha * y(3); -alpha * y(4) - g];

    % Definicija funkcije događaja za zaustavljanje integracije
    function [value, isterminal, direction] = pogodak_y(t, y, yB)
      value = y(2) - yB;   % kada y doseže yB
      isterminal = 1;      % zaustavi integraciju
      direction = 0;       % bilo kojim smjerom
    end
    opts = odeset('RelTol', 1e-11, 'Events', @pogodak_y);
    [t, y, tevent, yevent, ie] = ode45(F, interval, uvjeti);

  end

    % Početne granice za bisekciju
    theta_min = 0;
    theta_max = pi/2;

    % Tolerancija i maksimalan broj iteracija za bisekciju
    tol = 1e-6;
    max_iter = 100;

    % Metoda bisekcije
    for iter = 1:max_iter
        theta_mid = (theta_min + theta_max) / 2;

        % Simulacija za trenutni theta
        x_mid = solution(theta_mid, F, v0, yB);

        % Razlika x koordinate
        diff = x_mid - xB;

        if abs(diff) < tol
            fprintf('Optimalni kut θ je: %.6f radijana\n', theta_mid);
            return;
        end

        % Ažuriranje granica
        if diff > 0
            theta_max = theta_mid;
        else
            theta_min = theta_mid;
        end
    end

    fprintf('Metoda bisekcije nije konvergirala nakon %d iteracija\n', max_iter);
end


