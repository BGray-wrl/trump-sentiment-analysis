
library(ggplot2)
library(tidyverse)
library(ggthemes)


trump_shot<-as.Date("2024-07-13")
convention_speech<-as.Date("2024-07-18")
biden_drops<-as.Date("2024-07-21")

data<-read.csv("speech_sentiments.csv")%>%
  mutate(date=as.Date(month_day,format="%m-%d"))%>%
  filter(date!=trump_shot)


ylow=0.00#0.075 #0.1
yup=0.1# 0.2

data %>%
  ggplot(aes(x = date)) +
  # geom_smooth(aes(y = pos, color = "Positive"), method = "loess", span = 0.64, se=F, alpha = 0.15) +
  # geom_point(aes(y = pos, color = "Positive"), size = 2) +
  # geom_smooth(aes(y = neg, color = "Negative"), method = "loess", span = 0.64, se=F, alpha = 0.15) +
  # geom_point(aes(y = neg, color = "Negative"), size = 2) +
  geom_smooth(aes(y = pos-neg, color = "Pos - Neg"), method = "loess", span = 0.62, se = F) +
  geom_point(aes(y = pos-neg, color = "XX"), size = 2) +
  ylim(ylow,yup*1.1)+
  # 
  annotate("segment", x = trump_shot, xend = trump_shot, y = ylow, yend = yup, linetype = "dashed", color = "black", size = 0.1) +
  annotate("text", x = trump_shot, y = yup, label = "Assassination Attempt", vjust = 0, angle = 25, hjust = 0.5, size = 3) +
  
  geom_segment(aes(x = convention_speech, xend = convention_speech, y = ylow, yend = yup), linetype = "dashed", color = "black", size = 0.1) +
  annotate("text", x = convention_speech, y = yup, label = "Convention Speech", vjust = 0, hjust = 0.5, angle = 25, size = 3) +
  
  geom_segment(aes(x = biden_drops, xend = biden_drops, y = ylow, yend = yup), linetype = "dashed", color = "black", size = 0.1) +
  annotate("text", x = biden_drops, y = yup, label = "Biden Drops Out", vjust = 0, hjust = 0.5, angle = 25, size = 3) +
  
  scale_x_date(date_labels = "%b %d", date_breaks = "1 week", limits = c(min(data$date), max(data$date))) +
  
  scale_color_manual(name = "Legend", values = c("Positive" = "green","Negative"='orange', "Pos - Neg" = "darkred")) +
  # labs(title="Trump's Net Sentiment",subtitle = "\nMeasured as the difference between positive and negative sentiment")+
  
  theme_economist() +
  theme(
    plot.title = element_text(family = "Verdana", size = 18),
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    axis.text.x = element_text(hjust = 0.5, size = 12, color = "black"),
    axis.text.y = element_text(vjust = 0.5, hjust = 0, size = 8, color = "black"),
    axis.text.y.right = element_text(size = 15, color = "black"),
    legend.position = "right",
    legend.title = element_blank(),
    legend.text = element_text(size = 10),  # Adjust the size of the legend text
    panel.grid.major.x = element_blank(),  # Remove vertical grid lines
    panel.grid.minor.x = element_blank(),  # Remove minor vertical grid lines
    panel.grid.minor.y = element_blank(),  # Optional: Remove minor horizontal grid lines
    panel.grid.major.y = element_line(color = "lightgray"),  # Change horizontal grid line color for visibility
    axis.ticks.x = element_line(color = "black"),  # Add axis ticks
    axis.line.y = element_blank(),  # Add left y-axis line
    axis.line.x = element_line(color = "black")  # Add bottom x-axis line
  )



