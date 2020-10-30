install.packages("openxlsx")
install.packages("readxl")
install.packages("ggplot2")
install.packages("gplots")
install.packages("heatmap3")

install.packages ("readr")
install.packages ("dplyr")

library(gplots)
library(ggplot2)

library(openxlsx)
library(readxl)
library(readr)
library(dplyr)
library(esquisse)
library(heatmap3)



i2019<- read.xlsx ("/Users/Lenovo/Documents/tcc/imdb_web_scrapping_2019.xlsx")
i2018<- read.xlsx ("/Users/Lenovo/Documents/tcc/imdb_web_scrapping_2018.xlsx")
i2020<- read.xlsx ("/Users/Lenovo/Documents/tcc/imdb_web_scrapping_2020.xlsx")

years<- read.xlsx ("/Users/Lenovo/Documents/tcc/_Oscar_all_year.xlsx")

years2<- read.xlsx ("/Users/Lenovo/Documents/tcc/_Oscar_all_years 2.xlsx")

#grafico de bolha 2019
gI9<-ggplot(i2019, aes(i2019$Votos, y= i2019$Metascore, color=i2019$Imdb))+
  geom_point()
gI9+theme(legend.title = element_blank())+ggtitle("imdb")+ labs(x="votos", y="Metascore")

#grafico de bolha 2020
g20<-ggplot(i2020, aes(i2020$Votos, y= i2020$Metascore, color=i2020$Imdb))+
  geom_point()
g20+theme(legend.title = element_blank())+ggtitle("imdb")+ labs(x="votos", y="Metascore")

#grafico de bolha 2018
g18<-ggplot(i2018, aes(i2018$Votos, y= i2018$Metascore, color=i2018$Imdb))+
  geom_point()
g18+theme(legend.title = element_blank())+ggtitle("imdb")+ labs(x="votos", y="Metascore")

esquisser(years)


#boxplot da coluna dados 
boxplot(years$MetaScore)

boxplot(i2019$Metascore)
boxplot(i2018$Metascore)
boxplot(i2020$Metascore)

#boxplote metascore X imdb
bp <- boxplot(years2$MetaScore ~ years2$Ano,
        main= "metascore X Ano years",
        ylab="Meta.Score",
        xlab="Ano",
        col="blue",
        pch=16,
        horizontal= FALSE)


#boxplote 2019 metascore X imdb
bp <- boxplot(i2019$Metascore ~ i2019$ano,
              main= "2019 metascore X ano 2019",
              ylab="Meta.Score",
              xlab="ano 2019",
              col="blue",
              pch=16,
              horizontal= FALSE)

#boxplote 2018 metascore X imdb
bp <- boxplot(i2018$Metascore ~ i2018$Imdb,
              main= "2018 metascore X imdb",
              ylab="Meta.Score",
              xlab="imdb",
              col="blue",
              pch=16,
              horizontal= FALSE)

#boxplote 2020 metascore X imdb
bp <- boxplot(i2020$Metascore ~ i2020$Imdb,
              main= "2020 metascore X imdb",
              ylab="Meta.Score",
              xlab="imdb",
              col="blue",
              pch=16,
              horizontal= FALSE)

#visualizar os valores do boxblot  
bp


#heatmap da tabela years
years <- years %>% 
  mutate(
    Esp = reorder(id, MetaScore, function(x) max(x)),
  )
years

ggplot(years, aes(factor(MetaScore), Esp, fill = Imdb)) +
  geom_tile(color = "grey90") +
  labs(
    x = "IMDB", y = "MetaScore",
    fill = "MetaScore"
  ) +
  scale_fill_viridis_c(direction = -1) +
  theme_bw(8) +
  guides(col = guide_legend(reverse = TRUE))

#heatmap da tabela i2019
i2019 <-i2019 %>% 
  mutate(
    Esp = reorder(Filme, Metascore, function(x) max(x)),
  )
i2019
ggplot(i2019, aes(factor(Metascore), Esp, fill =Imdb)) +
  geom_tile(color = "grey90") +
  labs(
    x = "IMDB", y = "MetaScore",
    fill = "MetaScore2019"
  ) +
  scale_fill_viridis_c(direction = -1) +
  theme_bw(10) +
  guides(col = guide_legend(reverse = TRUE))

#heatmap da tabela i2018
i2018 <-i2018 %>% 
  mutate(
    Esp = reorder(Filme, Metascore, function(x) max(x)),
  )
i2018
ggplot(i2018, aes(factor(Metascore), Esp, fill =Imdb)) +
  geom_tile(color = "grey90") +
  labs(
    x = "IMDB", y = "MetaScore",
    fill = "MetaScore2018"
  ) +
  scale_fill_viridis_c(direction = -1) +
  theme_bw(10) +
  guides(col = guide_legend(reverse = TRUE))

#heatmap da tabela i2020
i2020 <-i2020 %>% 
  mutate(
    Esp = reorder(Filme, Metascore, function(x) max(x)),
  )
i2020
ggplot(i2020, aes(factor(Metascore), Esp, fill =Imdb)) +
  geom_tile(color = "grey90") +
  labs(
    x = "IMDB", y = "MetaScore",
    fill = "MetaScore2020"
  ) +
  scale_fill_viridis_c(direction = -1) +
  theme_bw(10) +
  guides(col = guide_legend(reverse = TRUE))

#heatmap
y<-data.matrix(years)
heatmap.2(y,main = "mapa de cores", trace = "none", margins = c(8,10))

yb<-colorRampPalette(c("blue", "green"))
heatmap.2(y, col= yb, main = "mapa de cores", trace = "none", margins = c(6,8))

#"limpar o grafico - quando nao funciona"
dev.off()



