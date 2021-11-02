from django.db import models
from django.utils import timezone


class Training(models.Model):

    title = models.CharField(max_length=64, default='Tower 90')
    date = models.DateField(blank=False, default=timezone.now())
    place = models.CharField(max_length=64, blank=False,)
    horse = models.CharField(max_length=64, blank=False, default='Koń')
    description = models.CharField(default='Brak', max_length=300)

# Przejazd 1 tarcze od 1 do 3
    a1 = models.CharField(max_length=10, default='', null=True, blank=False)
    b1 = models.CharField(max_length=10, default='', null=True, blank=False)
    c1 = models.CharField(max_length=10, default='', null=True, blank=False)
    run_1_time = models.DecimalField(default=18.00, decimal_places=3, max_digits=7, null=True, blank=False)
# Przejazd 2 tarcze od 1 do 3
    a2 = models.CharField(max_length=10, default='', null=True, blank=False)
    b2 = models.CharField(max_length=10, default='', null=True, blank=False)
    c2 = models.CharField(max_length=10, default='', null=True, blank=False)
    run_2_time = models.DecimalField(default=18.00, decimal_places=3, max_digits=7, null=True, blank=False)
# Przejazd 3 tarcze od 1 do 3
    a3 = models.CharField(max_length=10, default='', null=True, blank=False)
    b3 = models.CharField(max_length=10, default='', null=True, blank=False)
    c3 = models.CharField(max_length=10, default='', null=True, blank=False)
    run_3_time = models.DecimalField(default=18.00, decimal_places=3, max_digits=7, null=True, blank=False)
# Przejazd 4 tarcze od 1 do 3
    a4 = models.CharField(max_length=10, default='', null=True, blank=False)
    b4 = models.CharField(max_length=10, default='', null=True, blank=False)
    c4 = models.CharField(max_length=10, default='', null=True, blank=False)
    run_4_time = models.DecimalField(default=18.00, decimal_places=3, max_digits=7, null=True, blank=False)
# Przejazd 5 tarcze od 1 do 3
    a5 = models.CharField(max_length=10, default='', null=True, blank=False)
    b5 = models.CharField(max_length=10, default='', null=True, blank=False)
    c5 = models.CharField(max_length=10, default='', null=True, blank=False)
    run_5_time = models.DecimalField(default=18.00, decimal_places=3, max_digits=7, null=True, blank=False)
# Przejazd 6 tarcze od 1 do 3
    a6 = models.CharField(max_length=10, default='', null=True, blank=False)
    b6 = models.CharField(max_length=10, default='', null=True, blank=False)
    c6 = models.CharField(max_length=10, default='', null=True, blank=False)
    run_6_time = models.DecimalField(default=18.00, decimal_places=3, max_digits=7, null=True, blank=False)


#niepotrzebne do wyrzucenia
    result = models.DecimalField(decimal_places=3, max_digits=8, null=True, blank=True)



#wyniki generalne
    @property
    def result_general(self):
        tarcze = [self.a1, self.b1, self.c1, self.a2, self.b2, self.c2, self.a3, self.b3, self.c3, self.a4, self.b4,
                  self.c4, self.a5, self.b5, self.c5, self.a6, self.b6, self.c6]
        arrows_shoot = 0
        missed_arrows = 0
        arrows_in_target = 0
        arrows_in_target_no_points = 0
        counted_arrows = 0
        result = 0
        for liczymy in tarcze:
            for x in range(0, len(liczymy)):
                if liczymy[x] == "-":
                    missed_arrows += 1
                    arrows_shoot += 1
                elif liczymy[x] == '0':
                    arrows_in_target += 1
                    arrows_in_target_no_points += 1
                    arrows_shoot += 1
                elif liczymy[x] == '1' or liczymy[x] == '2' or liczymy[x] == '3' or liczymy[x] == '4' or liczymy[x] == '5':
                    arrows_in_target += 1
                    counted_arrows += 1
                    result += int(liczymy[x])
                    arrows_shoot += 1
        average_arrow = round((result/counted_arrows),2)
        counted_arrows_to_not_counted = counted_arrows/arrows_in_target_no_points

        return arrows_shoot, missed_arrows, arrows_in_target, arrows_in_target_no_points, counted_arrows,average_arrow,counted_arrows_to_not_counted ,result

#punkty suma
    # @property
    # def result_total(self):
    #     czasy = [self.run_1_time, self.run_2_time, self.run_3_time, self.run_4_time, self.run_5_time, self.run_6_time]
    #     time_points = 0
    #     for liczymy in czasy:
    #         if 18 < liczymy <= 20:
    #             time_points -= 5
    #         elif liczymy > 20:
    #             time_points = 0
    #             break
    #         else:
    #             time_points += (18 - liczymy)
    #     return (time_points + self.result_general[5])


#wyniki w przód
    @property
    def result_front(self):
        tarcze_f = [self.a1, self.a2, self.a3, self.a4, self.a5, self.a6]
        arrows_shoot_f = 0
        missed_arrows_f = 0
        arrows_in_target_f = 0
        arrows_in_target_no_points_f = 0
        counted_arrows_f = 0
        result_f = 0
        for liczymy_f in tarcze_f:
            for x in range(0, len(liczymy_f)):
                if liczymy_f[x] == "-":
                    missed_arrows_f += 1
                    arrows_shoot_f += 1
                elif liczymy_f[x] == '0':
                    arrows_in_target_f += 1
                    arrows_in_target_no_points_f += 1
                    arrows_shoot_f += 1
                elif liczymy_f[x] == '1' or liczymy_f[x] == '2' or liczymy_f[x] == '3' or liczymy_f[x] == '4' or liczymy_f[x] == '5':
                    arrows_in_target_f += 1
                    counted_arrows_f += 1
                    result_f += int(liczymy_f[x])
                    arrows_shoot_f += 1
        average_arrow_f = round((result_f / counted_arrows_f), 2)
        counted_arrows_to_not_counted_f = counted_arrows_f / arrows_in_target_f
        bad_luck_factor_f = round((counted_arrows_f / arrows_in_target_f * 100),2)
        return arrows_shoot_f, missed_arrows_f, arrows_in_target_f, arrows_in_target_no_points_f, counted_arrows_f,average_arrow_f,bad_luck_factor_f,counted_arrows_to_not_counted_f, result_f

# wyniki w bok

    @property
    def result_side(self):
        tarcze_s = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6]
        arrows_shoot_s = 0
        missed_arrows_s = 0
        arrows_in_target_s = 0
        arrows_in_target_no_points_s = 0
        counted_arrows_s = 0
        result_s = 0
        for liczymy_s in tarcze_s:
            for x in range(0, len(liczymy_s)):
                if liczymy_s[x] == "-":
                    missed_arrows_s += 1
                    arrows_shoot_s += 1
                elif liczymy_s[x] == '0':
                    arrows_in_target_s += 1
                    arrows_in_target_no_points_s += 1
                    arrows_shoot_s += 1
                elif liczymy_s[x] == '1' or liczymy_s[x] == '2' or liczymy_s[x] == '3' or liczymy_s[x] == '4' or \
                        liczymy_s[x] == '5':
                    arrows_in_target_s += 1
                    counted_arrows_s += 1
                    result_s += int(liczymy_s[x])
                    arrows_shoot_s += 1
        average_arrow_s = round((result_s / counted_arrows_s), 2)
        counted_arrows_to_not_counted_s = counted_arrows_s / arrows_in_target_s
        bad_luck_factor_s = round((counted_arrows_s / arrows_in_target_s * 100), 2)
        return arrows_shoot_s, missed_arrows_s, arrows_in_target_s, arrows_in_target_no_points_s, counted_arrows_s,average_arrow_s,bad_luck_factor_s, counted_arrows_to_not_counted_s,  result_s


#wyniki tył
    @property
    def result_back(self):
        tarcze_b = [self.c1, self.c2, self.c3, self.c4, self.c5, self.c6]
        arrows_shoot_b = 0
        missed_arrows_b = 0
        arrows_in_target_b = 0
        arrows_in_target_no_points_b = 0
        counted_arrows_b = 0
        result_b = 0
        for liczymy_b in tarcze_b:
            for x in range(0, len(liczymy_b)):
                if liczymy_b[x] == "-":
                    missed_arrows_b += 1
                    arrows_shoot_b += 1
                elif liczymy_b[x] == '0':
                    arrows_in_target_b += 1
                    arrows_in_target_no_points_b += 1
                    arrows_shoot_b += 1
                elif liczymy_b[x] == '1' or liczymy_b[x] == '2' or liczymy_b[x] == '3' or liczymy_b[x] == '4' or \
                        liczymy_b[x] == '5':
                    arrows_in_target_b += 1
                    counted_arrows_b += 1
                    result_b += int(liczymy_b[x])
                    arrows_shoot_b += 1
        average_arrow_b = round((result_b / counted_arrows_b), 2)
        counted_arrows_to_not_counted_b = counted_arrows_b / arrows_in_target_b
        bad_luck_factor_b = round((counted_arrows_b / arrows_in_target_b * 100), 2)
        return arrows_shoot_b, missed_arrows_b, arrows_in_target_b, arrows_in_target_no_points_b, counted_arrows_b,average_arrow_b,bad_luck_factor_b,counted_arrows_to_not_counted_b, result_b

#obliczenia procentów
    @property
    def procent(self):
        procent_general = []
        for x in self.result_general:
            procent_general.append(round((x*100/self.result_general[0]),2))
        return procent_general

    @property
    def procent_front(self):
        procent_front = []
        for y in self.result_front:
            procent_front.append(round((y * 100 / self.result_front[0]),2))
        return procent_front

    @property
    def procent_side(self):
        procent_side = []
        for z in self.result_side:
            procent_side.append(round((z * 100 / self.result_side[0]),2))
        return procent_side

    @property
    def procent_back(self):
        procent_back = []
        for w in self.result_back:
            procent_back.append(round((w * 100 / self.result_back[0]),2))
        return procent_back

    def __str__(self):
        return self.tytul_z_wynikiem()

    def tytul_z_wynikiem(self):
        return "{} ({})".format(self.title, self.result_general[6])


    class Meta:
        ordering = ('-date',)
